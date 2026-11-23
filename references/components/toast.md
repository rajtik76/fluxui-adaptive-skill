# Toast

- **Availability:** Flux (free).
- **Use:** Give short-lived feedback after an action.
- **Main tags:** `flux:toast`, `flux:toast.group`.

**Starter:**

```blade
<flux:toast />
```

## How to customize

- Mount the toast host in a layout, then dispatch transient feedback after actions.
- Heading, variant, inversion, link, and action options establish severity and next steps.
- Choose position, duration, permanence, and stacking behavior to avoid hiding important content.

## Capabilities

- **With heading** — A title can accompany toast text.
- **Variants** — Use success, warning, or danger styling for message severity.
- **Inverted** — tags `flux:toast`; settings `invert`.
- **Actions** — A toast action can dispatch an event that Livewire handles.
- **Links** — Attach a navigation link as the next step.
- **Positioning** — tags `flux:toast`; settings `position="top end"`.
- **Duration** — Set the lifetime in milliseconds; the default is five seconds.
- **Permanent** — Use zero duration to keep a toast visible until dismissed.
- **Stack** — tags `flux:toast.group`, `flux:toast`.

**Full page:** `references/source/components/toast.md` (bundled) or [live](https://fluxui.dev/components/toast.md). Read it for exact props, slots, and values.
