# Time picker

- **Availability:** Flux Pro.
- **Use:** Choose one or more clock times.
- **Main tags:** `flux:time-picker`.
- **Common props:** `wire:model`, `value`, `type`, `multiple`, `time-format`, `interval`, `min`, `max`, `unavailable`, `open-to`, `label`, `description`.

**Starter:**

```blade
<flux:time-picker wire:model="time" />
```

**Implementation:** Single values use `H:i`; a typed trigger or interval list can suit the task. Check multiple mode and time limits in the live page.

**Current source:** [Flux UI](https://fluxui.dev/components/time-picker.md).
