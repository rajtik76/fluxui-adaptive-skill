# Progress

- **Availability:** Flux (free).
- **Use:** Show completion on a measurable scale.
- **Main tags:** `flux:progress`.
- **Common props:** `value`, `max`, `color`.

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

## Component API

- **`flux:progress`** — props: `value` (default `0`), `max` (default `100`), `color`.

**Implementation:** Set `value` and optionally `max`; label, color, and height can clarify what is progressing.

**Current source:** [Flux UI](https://fluxui.dev/components/progress.md).
