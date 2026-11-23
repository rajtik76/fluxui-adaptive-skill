# Tooltip

- **Availability:** Flux (free).
- **Use:** Reveal brief supporting text on hover or focus.
- **Main tags:** `flux:tooltip`, `flux:tooltip.content`.

**Starter:**

```blade
<flux:tooltip content="Settings"><flux:button icon="cog-6-tooth" /></flux:tooltip>
```

## How to customize

- Provide short contextual text for an existing control without making it the only source of essential information.
- Set placement and offset to avoid obscuring nearby content.
- An info tooltip can hold richer content when a plain string is insufficient.

## Capabilities

- **Info tooltip** — tags `flux:heading`, `flux:tooltip`, `flux:button`, `flux:tooltip.content`; settings `toggleable`.
- **Position** — tags `flux:tooltip`, `flux:button`; settings `content="Settings"`, `position="top"`, `position="right"`, `position="bottom"`, `position="left"`.

**Full page:** `references/source/components/tooltip.md` (bundled) or [live](https://fluxui.dev/components/tooltip.md). Read it for exact props, slots, and values.
