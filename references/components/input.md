# Input

- **Availability:** Flux (free).
- **Use:** Collect short text and other native input values.
- **Main tags:** `flux:input`, `flux:input.group`, `flux:input.group.prefix`, `flux:input.group.suffix`.
- **Common props:** `wire:model`, `label`, `description`, `description:trailing`, `placeholder`, `size`, `variant`, `disabled`, `readonly`, `invalid`, `multiple`, `mask`.

**Starter:**

```blade
<flux:input wire:model="email" type="email" label="Email" />
```

**Implementation:** Bind with Livewire and use label, description, and error shorthand or a full field. Check type, mask, icons, and disabled/readonly behavior.

**Current source:** [Flux UI](https://fluxui.dev/components/input.md).
