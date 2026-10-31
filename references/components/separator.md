# Separator

- **Availability:** Flux (free).
- **Use:** Create a visual boundary between regions.
- **Main tags:** `flux:separator`.
- **Common props:** `vertical`, `variant`, `text`, `orientation`.

**Starter:**

```blade
<flux:separator />
```

## How to customize

- Use a horizontal divider between sections or a vertical divider between adjacent controls.
- A text label can explain the boundary.
- Subtle styling or limited height prevents a separator from dominating the layout.

## Capabilities

- **With text** — tags `flux:separator`; settings `text`.
- **Vertical** — tags `flux:separator`; settings `vertical`.
- **Limited height** — tags `flux:separator`; settings `vertical`.
- **Subtle** — tags `flux:separator`; settings `vertical`, `variant="subtle"`.

## Component API

- **`flux:separator`** — props: `vertical`, `variant` (values `subtle`), `text`, `orientation` (values `horizontal`, `vertical`; default `horizontal`); classs: `my-*`.

**Implementation:** Use horizontal separation by default; set `vertical` where the layout calls for it. Text and subtle treatments are available.

**Current source:** [Flux UI](https://fluxui.dev/components/separator.md).
