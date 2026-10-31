# Toast

- **Availability:** Flux (free).
- **Use:** Give short-lived feedback after an action.
- **Main tags:** `flux:toast`, `flux:toast.group`.
- **Common props:** `position`, `invert`.

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

## Component API

- **`flux:toast`** — props: `position` (values `bottom end`, `bottom center`, `bottom start`, `top end`, `top center`, `top start`), `invert` (default `false`).
- **`flux:toast.group`** — props: `position` (values `bottom end`, `bottom center`, `bottom start`, `top end`, `top center`, `top start`), `expanded` (default `false`).

**Implementation:** Mount `flux:toast` in the layout and trigger messages via `Flux::toast()` or the supported JavaScript API. Variants, position, and duration are configurable.

**Current source:** [Flux UI](https://fluxui.dev/components/toast.md).
