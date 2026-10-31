# Checkbox

- **Availability:** Flux (free).
- **Use:** Collect one or more boolean choices.
- **Main tags:** `flux:checkbox`, `flux:checkbox.group`, `flux:checkbox.all`.
- **Common props:** `wire:model`, `label`, `description`, `value`, `checked`, `indeterminate`, `disabled`, `invalid`.

**Starter:**

```blade
<flux:checkbox wire:model="accepted" label="Accept terms" />
```

**Implementation:** Bind a single checkbox or a checkbox group with Livewire. Use `value` for grouped options; `flux:checkbox.all` supports select-all behavior.

**Current source:** [Flux UI](https://fluxui.dev/components/checkbox.md).
