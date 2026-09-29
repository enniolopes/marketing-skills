# marketing-skills

[![validate](https://github.com/enniolopes/marketing-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/enniolopes/marketing-skills/actions/workflows/validate.yml)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](LICENCE)

Portable Agent Skills for brand and marketing work.

## Skills

| Skill | What it does |
|---|---|
| [**Branding Studio**](skills/branding-studio/) | Creates and operates brand systems: strategy, creative direction, identity, touchpoints, brand books, audits, and evolution. |
| [**Landing Page**](skills/landing-page/) | Researches, designs, builds, and refines high-end marketing landing pages and homepages. |

## Install

### Claude Code

Add this marketplace once:

```text
/plugin marketplace add enniolopes/marketing-skills
```

Then install the skill you want:

```text
/plugin install branding-studio@enniolopes
/plugin install landing-page@enniolopes
```

### ChatGPT

Where Agent Skills are supported, use the skill ZIPs from [GitHub Releases](https://github.com/enniolopes/marketing-skills/releases).

Workspace admins can also import this repository as a plugin marketplace:

```text
https://github.com/enniolopes/marketing-skills
```

### Gemini CLI

Install a standalone skill directly from the repository:

```bash
gemini skills install https://github.com/enniolopes/marketing-skills.git --path skills/<name>
```

### Other Agent Skills hosts

Install the chosen `skills/<name>/` directory with the host's normal Agent Skills flow.

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md). The repository's blocking validation is:

```bash
python development/validate.py
```
