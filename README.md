# Flux UI Adaptive Skill

An **unofficial agent skill** for Livewire Flux UI. It builds on the workflow of Laravel Boost's MIT-licensed Flux UI skill and adds live discovery. The bundle contains concise notes for all 52 components listed by Flux UI on 31 October 2026, including 21 Pro components. An optional Python helper provides SHA-256 source checks and a private offline cache.

## What it does

1. The agent reads the current [Flux UI `llms.txt`](https://fluxui.dev/llms.txt) with its available web tool, then merges it with `manifest.json`. Newly released components enter the router immediately.
2. For selected components, the agent reads official Markdown, or the corresponding HTML page when its web tool cannot open `.md`. Without a reliable raw-byte hash check, it uses the live page directly. With the optional helper, an unchanged page selects the concise bundled note; a changed or new page selects the live page immediately.
3. The helper caches fetched pages privately. If Flux UI is unavailable later, the agent can use an accessible cache or a bundled note, labeled unverified.

The Flux UI Markdown pages are **not distributed in this repository**. Each component has an original short note, starter snippet, selected API names, and a link to the official page. The skill targets Flux v2. A component released after the bundled snapshot must be fetched at least once before it can work offline. When a request goes beyond a note or the agent is unsure about an API, it reads the current official Markdown page; if the web tool cannot open `.md`, it uses the corresponding HTML page.

## Install

Put this entire repository in your agent's skills directory as `fluxui-adaptive`, preserving `SKILL.md`, `manifest.json`, `references/`, and `scripts/`. The skill name is distinct from Laravel Boost's `fluxui-development`, so both can be installed without a name collision. Follow your agent's normal skill installation instructions for the exact directory or upload method.

## Agent compatibility

The basic live workflow needs an agent that can read the skill files and fetch Flux UI documentation. It does **not** require Python or shell access. The exact hash comparison and automatic cache need a shell, Python 3.10+, and a writable cache; no third-party packages are needed. On Windows, `py -3` may replace `python3`.

Installing a skill cannot grant a runtime, network access, or bypass an agent host's approval policy. Some hosts may ask before running a script or fetching a page; this repository cannot guarantee prompt-free operation in every agent.

## Optional helper

```bash
python3 scripts/fluxui_docs.py catalog
python3 scripts/fluxui_docs.py show date-picker
python3 scripts/fluxui_docs.py show datetime-picker
python3 scripts/fluxui_docs.py show datetime-picker --offline
```

The cache defaults to `~/.cache/fluxui-development`. Set `FLUXUI_SKILL_CACHE` to use another directory. Add `--json` for structured output. See [SKILL.md](SKILL.md) for the agent workflow.

## Maintaining the bundle

Run `python3 scripts/fluxui_docs.py audit` to compare every live component page with `manifest.json`. The scheduled GitHub Actions workflow runs this check weekly and opens or updates an issue when it finds a new, changed, or removed component. The skill uses live documentation immediately when a bundled hash differs; updating the notes is a separate maintenance task.

## Verify

```bash
python3 -m unittest discover -s tests -v
```

## Attribution

This is an independent project, not affiliated with Livewire or Flux UI. The skill workflow adapts [Laravel Boost's Flux UI skill](https://github.com/laravel/boost/tree/main/.ai/fluxui-pro/skill/fluxui-development), licensed under MIT; its copyright notice is retained in [LICENSE.md](LICENSE.md).
