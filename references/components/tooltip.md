# Tooltip

- **Availability:** Flux (free).
- **Use:** Reveal brief supporting text on hover or focus.
- **Main tags:** `flux:tooltip`, `flux:tooltip.content`.
- **Common props:** `content`, `position`, `align`, `disabled`, `gap`, `offset`, `toggleable`, `interactive`, `kbd`.

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

## Component API

- **`flux:tooltip`** — props: `content`, `position` (values `top`, `right`, `bottom`, `left`), `align` (values `center`, `start`, `end`), `disabled`, `gap` (default `5`), `offset` (default `0`), `toggleable`, `interactive`, `kbd`.
- **`flux:tooltip.content`** — props: `kbd`.

**Implementation:** Wrap the target in `flux:tooltip` and supply `content`; placement and richer interactive content are available.

**Current source:** [Flux UI](https://fluxui.dev/components/tooltip.md).
