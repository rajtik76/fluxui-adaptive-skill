# Flux UI Adaptive Skill

An **unofficial prototype** of an agent skill for Livewire Flux UI. It builds on the workflow of Laravel Boost's MIT-licensed Flux UI skill and adds live discovery, SHA-256 source checks, and a private offline cache.

## What it does

1. `catalog` reads the current [Flux UI `llms.txt`](https://fluxui.dev/llms.txt) and merges it with the entries bundled here. Newly released components appear in the router immediately.
2. `show` fetches the selected component's official Markdown page. When its SHA-256 matches a reviewed bundled entry, it returns the short local note. A changed or new component uses the live page immediately.
3. Fetched pages stay in the user's local cache. If the site is unavailable later, `show` uses the cached page or a bundled note and marks it unverified.

The Flux UI Markdown pages are **not distributed in this repository**. The two bundled notes are short, original prototype content. This prototype currently targets Flux v2 and includes reviewed notes for Date picker and Time picker. A new component must be fetched at least once before it can work offline.

## Try it

Requires Python 3.10 or newer; no third-party Python packages are needed.

```bash
python3 scripts/fluxui_docs.py catalog
python3 scripts/fluxui_docs.py show date-picker
python3 scripts/fluxui_docs.py show datetime-picker
python3 scripts/fluxui_docs.py show datetime-picker --offline
```

The cache defaults to `~/.cache/fluxui-development`. Set `FLUXUI_SKILL_CACHE` to use another directory. Add `--json` for structured output. See [SKILL.md](SKILL.md) for the agent workflow.

## Verify

```bash
python3 -m unittest discover -s tests -v
```

## Attribution

This is an independent project, not affiliated with Livewire or Flux UI. The skill workflow adapts [Laravel Boost's Flux UI skill](https://github.com/laravel/boost/tree/main/.ai/fluxui-pro/skill/fluxui-development), licensed under MIT; its copyright notice is retained in [LICENSE.md](LICENSE.md).
