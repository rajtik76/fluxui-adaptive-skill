# Popover

- **Availability:** Flux Pro.
- **Use:** Show custom floating content from a trigger.
- **Main tags:** `flux:dropdown`, `flux:popover`.
- **Common props:** `position`, `align`, `hover`, `wire:model`.

**Starter:**

```blade
<flux:dropdown><flux:button>Details</flux:button><flux:popover>More information</flux:popover></flux:dropdown>
```

**Implementation:** Wrap the trigger and `flux:popover` in `flux:dropdown`. Configure placement or hover behavior on the dropdown.

**Current source:** [Flux UI](https://fluxui.dev/components/popover.md).
