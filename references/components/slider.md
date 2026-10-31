# Slider

- **Availability:** Flux Pro.
- **Use:** Adjust a numeric value by dragging along a track.
- **Main tags:** `flux:slider`, `flux:slider.tick`.
- **Common props:** `range`, `min`, `max`, `step`, `big-step`, `min-steps-between`, `tick:position`, `track:class`, `thumb:class`.

**Starter:**

```blade
<flux:slider wire:model="amount" min="0" max="100" />
```

**Implementation:** Bind with Livewire; set `min`, `max`, and `step`. Range, ticks, and an accompanying input are available for more precise use.

**Current source:** [Flux UI](https://fluxui.dev/components/slider.md).
