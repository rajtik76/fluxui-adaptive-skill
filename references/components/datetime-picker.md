# Datetime picker

- **Availability:** Flux Pro.
- **Use:** Choose a date and time together for a scheduled event.
- **Main tags:** `flux:datetime-picker`, `flux:datetime-picker.button`.
- **Common props:** `wire:model`, `value`, `name`, `mode`, `placeholder`, `size`, `time`, `interval`, `time-format`, `min`, `max`, `min-time`.

**Starter:**

```blade
<flux:datetime-picker wire:model="startsAt" />
```

**Implementation:** Single values use `Y-m-d\TH:i`; `mode="range"` accepts start/end datetimes. Configure time input, interval, limits, and unavailable slots as needed.

**Current source:** [Flux UI](https://fluxui.dev/components/datetime-picker.md).
