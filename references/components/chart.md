# Chart

- **Availability:** Flux Pro.
- **Use:** Visualize Livewire data with Flux chart primitives.
- **Main tags:** `flux:chart`, `flux:chart.svg`, `flux:chart.line`, `flux:chart.area`, `flux:chart.point`, `flux:chart.pie`.
- **Common props:** `wire:model`, `value`, `horizontal`, `class`.

**Starter:**

```blade
<flux:chart wire:model="data"><flux:chart.svg><flux:chart.line field="visitors" /></flux:chart.svg></flux:chart>
```

**Implementation:** Bind an array of named data points; nest `flux:chart.svg` and a line, area, bar, or other plot. Plot `field` names must match data keys.

**Current source:** [Flux UI](https://fluxui.dev/components/chart.md).
