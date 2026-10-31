# Textarea

- **Availability:** Flux (free).
- **Use:** Collect longer free-form text.
- **Main tags:** `flux:textarea`.
- **Common props:** `wire:model`, `placeholder`, `label`, `description`, `description:trailing`, `badge`, `rows`, `resize`, `invalid`.

**Starter:**

```blade
<flux:textarea wire:model="notes" label="Notes" />
```

**Implementation:** Bind with Livewire; use rows, resize, or auto-sizing behavior to fit the expected length.

**Current source:** [Flux UI](https://fluxui.dev/components/textarea.md).
