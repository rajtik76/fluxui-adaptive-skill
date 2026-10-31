# Calendar

- **Availability:** Flux Pro.
- **Use:** Select dates directly in a calendar view.
- **Main tags:** `flux:calendar`.
- **Common props:** `wire:model`, `value`, `mode`, `min`, `max`, `unavailable`, `size`, `start-day`, `months`, `min-range`, `max-range`, `open-to`.

**Starter:**

```blade
<flux:calendar wire:model="selectedDate" />
```

**Implementation:** Bind with `wire:model`; `mode` supports single, multiple, and range selection. Check date limits and unavailable dates for constrained booking flows.

**Current source:** [Flux UI](https://fluxui.dev/components/calendar.md).
