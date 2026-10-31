# Date picker

- **Availability:** Flux Pro.
- **Use:** Choose a date or date interval from an overlay calendar.
- **Main tags:** `flux:date-picker`, `flux:date-picker.input`, `flux:date-picker.button`.
- **Common props:** `wire:model`, `value`, `type`, `mode`, `min-range`, `max-range`, `min`, `max`, `unavailable`, `open-to`, `force-open-to`, `months`.

**Starter:**

```blade
<flux:date-picker wire:model="date" />
```

**Implementation:** A single date uses `Y-m-d`; `mode="range"` enables intervals. Check limits, unavailable dates, presets, and trigger variants in the live page when needed.

**Current source:** [Flux UI](https://fluxui.dev/components/date-picker.md).
