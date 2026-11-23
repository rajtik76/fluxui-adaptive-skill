# Progress

- **Availability:** Flux (free).
- **Use:** Show completion on a measurable scale.
- **Main tags:** `flux:progress`.

**Starter:**

```blade
<flux:progress value="75" />
```

## How to customize

- Set the current value and optionally a non-percentage maximum.
- Color, height, labels, and value display communicate both state and scale.
- Keep the value synchronized with the underlying operation when progress is controlled by Livewire.

## Capabilities

- **Max** — tags `flux:progress`; settings `max="7"`.
- **Color** — tags `flux:progress`; settings `color="purple"`.
- **Height** — tags `flux:progress`.
- **With label** — tags `flux:field`, `flux:label`, `flux:progress`, `flux:description`; settings `color="blue"`.
- **Display value** — tags `flux:field`, `flux:label`, `flux:progress`.
- **Controlled** — tags `flux:slider`, `flux:progress`.

**Full page:** `references/source/components/progress.md` (bundled) or [live](https://fluxui.dev/components/progress.md). Read it for exact props, slots, and values.
