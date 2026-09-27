# skills

[![validate](https://github.com/enniolopes/skills/actions/workflows/validate.yml/badge.svg)](https://github.com/enniolopes/skills/actions/workflows/validate.yml)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](LICENCE)

Portable capabilities for AI assistants.

## Capabilities

| Capability | Type | Use it for |
|---|---|---|
| [**Branding Studio**](skills/branding-studio/) | Skill | Create, audit, apply, and evolve brands and identity systems. |
| [**Landing Page**](skills/landing-page/) | Skill | Research, design, build, and refine marketing landing pages and homepages. |

## Claude Code

Add the marketplace once:

```text
/plugin marketplace add enniolopes/skills
```

Install the capability you want:

```text
/plugin install branding-studio@enniolopes
/plugin install landing-page@enniolopes
```

`research` uses `explorer` for structural exploration, so install both when using the research system:

```text
/plugin install research@enniolopes
/plugin install explorer@enniolopes
```

Then describe the job normally. The Research system now lives in the [standalone research repository](https://github.com/enniolopes/research).

## ChatGPT

For standalone Skills, where Skills are available on your account, upload the skill ZIP from [GitHub Releases](https://github.com/enniolopes/skills/releases).

Workspace admins can also import this repository as a plugin marketplace from **Workspace settings → Plugins → Add → Import marketplace** using:

```text
https://github.com/enniolopes/skills
```

## Gemini CLI

Standalone Skills can be installed directly from this repository:

```bash
gemini skills install https://github.com/enniolopes/skills.git --path skills/<name>
```

## Other Agent Skills hosts

Install the chosen `skills/<name>/` directory using the host's normal Agent Skills flow.

Standalone Skills are the most portable unit. `research` is a composed system and currently targets plugin hosts such as Claude Code.
