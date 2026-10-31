# Timeline

- **Availability:** Flux Pro.
- **Use:** Present events or steps in sequence.
- **Main tags:** `flux:timeline`, `flux:timeline.item`, `flux:timeline.indicator`, `flux:timeline.content`, `flux:timeline.block`, `flux:timeline.subgrid`.
- **Common props:** `horizontal`, `align`, `size`.

**Starter:**

```blade
<flux:timeline><flux:timeline.item><flux:timeline.indicator /><flux:timeline.content>Event</flux:timeline.content></flux:timeline.item></flux:timeline>
```

**Implementation:** Nest items with indicators and content. Horizontal orientation, size, and status styles cover different densities.

**Current source:** [Flux UI](https://fluxui.dev/components/timeline.md).
