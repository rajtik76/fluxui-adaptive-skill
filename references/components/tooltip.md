# Tooltip

- **Availability:** Flux (free).
- **Use:** Reveal brief supporting text on hover or focus.
- **Main tags:** `flux:tooltip`, `flux:tooltip.content`.
- **Common props:** `content`, `position`, `align`, `disabled`, `gap`, `offset`, `toggleable`, `interactive`, `kbd`.

**Starter:**

```blade
<flux:tooltip content="Settings"><flux:button icon="cog-6-tooth" /></flux:tooltip>
```

**Implementation:** Wrap the target in `flux:tooltip` and supply `content`; placement and richer interactive content are available.

**Current source:** [Flux UI](https://fluxui.dev/components/tooltip.md).
