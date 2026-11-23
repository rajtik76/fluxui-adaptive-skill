# Flux UI Adaptive Skill

An **unofficial agent skill** for Livewire Flux UI, including Flux Pro. It builds on the workflow of Laravel Boost's MIT-licensed Flux UI skill and adds the official documentation, live discovery of new pages, and an automated update process.

## What it does

1. The agent reads the current [Flux UI `llms.txt`](https://fluxui.dev/llms.txt) and merges it with `manifest.json`. Newly released guides, layouts, and components are available immediately.
2. Short notes in `references/` help the agent choose a component or variant without reading every page.
3. For implementation, the agent reads the full official Markdown page bundled in `references/source/`. When the installed Flux release is newer than the bundle, or the page lacks a feature, it reads the live page instead.
4. An optional Python helper compares live pages with the bundle by SHA-256 and privately caches pages that differ from the bundle for offline use.

## Install

Put this repository in your agent's skills directory as `fluxui-adaptive`, preserving `SKILL.md`, `manifest.json`, `references/`, and `scripts/`. The name differs from Laravel Boost's `fluxui-development`, so both can be installed side by side.

## Agent compatibility

The basic workflow needs an agent that can read the skill files; fetching live pages additionally needs a web tool. Python is **not** required. The optional helper needs a shell and Python 3.10+, with no third-party packages; on Windows, `py -3` may replace `python3`.

Installing a skill cannot grant a runtime or network access, or bypass an agent host's approval policy. Some hosts ask before running a script or fetching a page.

## Optional helper

```bash
python3 scripts/fluxui_docs.py catalog
python3 scripts/fluxui_docs.py brief date-picker
python3 scripts/fluxui_docs.py show date-picker
python3 scripts/fluxui_docs.py show sidebar --offline
```

The cache defaults to `~/.cache/fluxui-adaptive`. Set `FLUXUI_SKILL_CACHE` to use another directory. Add `--json` for structured output.

## Maintaining the bundle

`python3 scripts/fluxui_docs.py audit` compares every live page with the bundle. `python3 scripts/fluxui_docs.py sync` downloads new and changed pages, removes deleted ones, and updates `manifest.json`. A weekly GitHub Actions workflow runs `sync` and opens or updates a pull request with the changes. Short notes are not regenerated; the pull request lists the ones worth reviewing.

The workflow needs **Settings → Actions → General → Allow GitHub Actions to create and approve pull requests** enabled.

## Verify

```bash
python3 -m unittest discover -s tests -v
```

## Attribution and license

This is an independent project, not affiliated with Livewire or Flux UI.

- The pages in `references/source/` are the official [Flux UI](https://fluxui.dev) documentation, © Flux UI, bundled with the permission of the Flux UI team. They are not covered by this repository's MIT license.
- The skill workflow adapts [Laravel Boost's Flux UI skill](https://github.com/laravel/boost/tree/main/.ai/fluxui-pro/skill/fluxui-development), licensed under MIT; its copyright notice is retained in [LICENSE.md](LICENSE.md).
- The skill contains no Flux component source code. Flux Pro components still require a Flux Pro license.
