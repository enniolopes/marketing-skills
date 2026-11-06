import json
import os
import tempfile
import unittest
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[3]
ROOT = REPO_ROOT / "skills" / "branding-studio"
sys.path.insert(0, str(ROOT / "scripts"))

import asset_checks
import book_checks
import validate_structure


BOOK = """<!doctype html><html lang="pt-BR"><head><title>Manual</title>
<style>
@font-face {{ font-family: X; src: url(data:font/woff2;base64,AAAA); }}
@media print {{ body {{ margin: 0; }} }}
.cover {{ background: url("logo/marca.svg"); }}
</style></head><body>
<img src="logo/marca.svg" alt="Marca principal">
<img srcset="foto/prato.jpg 1x, foto/prato%202x.jpg 2x" src="foto/prato.jpg" alt="Prato">
<a href="logo/marca.svg" download>Baixar</a>
<a href="https://example.org/licenca">Licença</a>
{extra}
</body></html>"""

SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><rect width="10" height="10"/></svg>'


def write_package(root: Path, extra: str = "", orphan: bool = False, contract: bool = False):
    (root / "logo").mkdir()
    (root / "foto").mkdir()
    (root / "logo" / "marca.svg").write_text(SVG)
    (root / "foto" / "prato.jpg").write_bytes(b"\xff\xd8\xff")
    (root / "foto" / "prato 2x.jpg").write_bytes(b"\xff\xd8\xff")
    (root / "index.html").write_text(BOOK.format(extra=extra))
    if orphan:
        (root / "foto" / "antiga.jpg").write_bytes(b"\xff\xd8\xff")
    if contract:
        (root / "brand-spec.json").write_text(json.dumps({"meta": {"schema_version": 5}}))
        (root / "brand-report.md").write_text("# report\n")


def valid_spec():
    spec = json.loads((ROOT / "templates" / "brand-spec.template.json").read_text())
    spec["meta"].update({"brand_name": "Northstar", "tier": "full", "touchpoints": ["website"]})
    spec["strategy"]["brand_job"]["statement"] = "Make a complex product legible to technical buyers."
    spec["strategy"]["audience"].update({"primary": "Technical operations leaders.", "language": "en"})
    spec["strategy"]["offer_truth"] = {
        "statement": "The product exposes operational structure from workflow data.",
        "basis": "Product documentation, section 2.",
    }
    spec["strategy"]["alternatives"] = ["manual analysis"]
    spec["strategy"]["position"]["statement"] = "Operational clarity without another generic AI layer."
    spec["strategy"]["right_to_win"]["statement"] = "Domain-specific workflow data."
    spec["strategy"]["desired_meaning"] = "Precise operational clarity."
    spec["creative_direction"].update({
        "thesis": "Reveal the hidden operating layer.",
        "principles": ["Reveal structure progressively."],
        "signature": "Layered reveal behavior.",
    })
    spec["visual"] = {
        "logo": {"production": {"status": "final", "master_format": "svg", "master_path": "assets/logo.svg"}},
        "tokens": {"color": {"ink": {"$type": "color", "$value": "#101010", "name": "Ink"}}},
    }
    return spec


class BrandingStudioScriptTests(unittest.TestCase):
    def test_sparse_contract_is_valid(self):
        spec = valid_spec()
        spec["meta"]["version"] = "2.3.0"
        self.assertEqual(validate_structure.validate(spec)["verdict"], "STRUCTURALLY_VALID")

    def test_template_declares_current_schema(self):
        spec = json.loads((ROOT / "templates" / "brand-spec.template.json").read_text())
        self.assertEqual(spec["meta"]["schema_version"], validate_structure.SCHEMA_VERSION)

    def test_audience_language_is_required(self):
        spec = valid_spec()
        del spec["strategy"]["audience"]["language"]
        self.assertEqual(validate_structure.validate(spec)["verdict"], "STRUCTURALLY_INVALID")

    def test_provisional_contract_may_omit_strategy_hypotheses(self):
        spec = valid_spec()
        spec["meta"]["tier"] = "provisional"
        spec["visual"]["logo"]["production"]["status"] = "concept"
        del spec["strategy"]["position"]
        del spec["strategy"]["right_to_win"]
        del spec["strategy"]["desired_meaning"]
        spec["creative_direction"]["criteria"] = ["Reads as a named person answering, not software."]
        report = validate_structure.validate(spec)
        self.assertEqual(report["verdict"], "STRUCTURALLY_VALID")
        self.assertEqual(sum("required before tier full" in w for w in report["warnings"]), 3)

    def test_full_contract_requires_strategy_fields(self):
        spec = valid_spec()
        del spec["strategy"]["right_to_win"]
        report = validate_structure.validate(spec)
        self.assertEqual(report["verdict"], "STRUCTURALLY_INVALID")
        self.assertTrue(any("full-tier contract field missing: strategy.right_to_win" in f for f in report["failures"]))

    def test_ledger_blocks_are_rejected(self):
        spec = valid_spec()
        spec["evidence"] = [{"id": "E-001", "claim": "x", "kind": "fact", "source": "y", "status": "active"}]
        spec["open_questions"] = ["Confirm the green."]
        report = validate_structure.validate(spec)
        self.assertEqual(report["verdict"], "STRUCTURALLY_INVALID")
        self.assertTrue(any("evidence, open_questions" in f for f in report["failures"]))

    def test_final_logo_requires_a_master(self):
        spec = valid_spec()
        del spec["visual"]["logo"]["production"]["master_path"]
        self.assertEqual(validate_structure.validate(spec)["verdict"], "STRUCTURALLY_INVALID")

    def test_schema_4_contract_is_legacy_with_warning(self):
        legacy = valid_spec()
        legacy["meta"]["schema_version"] = 4
        del legacy["strategy"]["audience"]["language"]
        legacy["evidence"] = [{
            "id": "E-001", "claim": "x", "kind": "fact", "source": "y", "status": "superseded",
        }]
        legacy["strategy"]["offer_truth"]["evidence_refs"] = ["E-001"]
        report = validate_structure.validate(legacy)
        self.assertEqual(report["verdict"], "STRUCTURALLY_VALID")
        self.assertTrue(any("legacy schema 4" in w for w in report["warnings"]))

    def test_schema_4_evidence_references_must_resolve(self):
        legacy = valid_spec()
        legacy["meta"]["schema_version"] = 4
        legacy["evidence"] = [{"id": "E-001", "claim": "x", "kind": "fact", "source": "y", "status": "active"}]
        legacy["strategy"]["offer_truth"]["evidence_refs"] = ["E-999"]
        self.assertEqual(validate_structure.validate(legacy)["verdict"], "STRUCTURALLY_INVALID")

    def test_pre_schema_contract_remains_operable(self):
        legacy = {
            "meta": {"version": "3.0.0", "tier": "full", "touchpoints": ["web"]},
            "research": {"findings": []},
            "visual": {"typography": {"hierarchy": {"mode": "custom", "rules": ["Explicit relationship"]}}},
        }
        self.assertEqual(validate_structure.validate(legacy)["verdict"], "STRUCTURALLY_VALID")

    def test_self_contained_package_is_valid(self):
        with tempfile.TemporaryDirectory() as tmp:
            write_package(Path(tmp))
            report = book_checks.inspect_folder(tmp)
        self.assertEqual(report["verdict"], "PACKAGE_VALID", report["failures"])
        self.assertTrue(any("lang=pt-BR" in p for p in report["passed"]))

    def test_flag_words_warn_only_outside_example_elements(self):
        extra = ('<p>Nossa marca é única e elegante! Use 24 px de margem.</p>'
                 '<blockquote>Única no mercado! Elegante como você.</blockquote>'
                 '<figure><img src="logo/marca.svg" alt="Errado"><figcaption>Errado: logo inovador esticado</figcaption></figure>')
        with tempfile.TemporaryDirectory() as tmp:
            write_package(Path(tmp), extra=extra)
            report = book_checks.inspect_folder(tmp)
        self.assertEqual(report["verdict"], "PACKAGE_VALID", report["failures"])
        flagged = [w for w in report["warnings"] if "flag words" in w]
        self.assertEqual(len(flagged), 1)
        self.assertIn("única×1", flagged[0])
        self.assertIn("elegante×1", flagged[0])
        self.assertNotIn("inovador", flagged[0])
        self.assertTrue(any("1 exclamation mark" in w for w in report["warnings"]))

    def test_missing_lang_warns_but_does_not_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            write_package(Path(tmp))
            html = (Path(tmp) / "index.html").read_text().replace('<html lang="pt-BR">', "<html>")
            (Path(tmp) / "index.html").write_text(html)
            report = book_checks.inspect_folder(tmp)
        self.assertEqual(report["verdict"], "PACKAGE_VALID", report["failures"])
        self.assertTrue(any("no <html lang>" in w for w in report["warnings"]))
        self.assertEqual(report["counts"]["images"], 2)

    def test_package_defects_are_each_named(self):
        extra = (
            '<script src="app.js"></script>'
            '<link rel="stylesheet" href="https://fonts.example/css">'
            '<img src="/foto/prato.jpg">'
            '<img src="foto/nada.jpg" alt="">'
        )
        with tempfile.TemporaryDirectory() as tmp:
            write_package(Path(tmp), extra=extra, orphan=True, contract=True)
            report = book_checks.inspect_folder(tmp)
        self.assertEqual(report["verdict"], "PACKAGE_INVALID")
        joined = "\n".join(report["failures"])
        for expected in ("scripts found", "external requests", "absolute paths",
                         "unresolved references", "without alt", "contract served",
                         "report served", "never reaches"):
            self.assertIn(expected, joined)
        self.assertTrue(any("empty alt" in w for w in report["warnings"]))

    def test_missing_print_stylesheet_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            write_package(Path(tmp))
            html = (Path(tmp) / "index.html").read_text().replace("@media print", "@media screen")
            (Path(tmp) / "index.html").write_text(html)
            report = book_checks.inspect_folder(tmp)
        self.assertTrue(any("print stylesheet" in f for f in report["failures"]))

    def test_raster_content_blocks_svg_master(self):
        svg = '<svg xmlns="http://www.w3.org/2000/svg"><image href="data:image/png;base64,AAAA"/></svg>'
        with tempfile.NamedTemporaryFile("w", suffix=".svg", delete=False) as handle:
            handle.write(svg)
            path = handle.name
        try:
            self.assertEqual(asset_checks.inspect_svg(path)["verdict"], "SVG_STRUCTURE_INVALID")
        finally:
            os.unlink(path)


if __name__ == "__main__":
    unittest.main()
