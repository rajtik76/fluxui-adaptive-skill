# Field

- **Availability:** Flux (free).
- **Use:** Keep a form control, label, help text, and validation error together.
- **Main tags:** `flux:field`, `flux:label`, `flux:description`, `flux:error`, `flux:fieldset`, `flux:legend`.
- **Common props:** `variant`.

**Starter:**

```blade
<flux:field><flux:label>Email</flux:label><flux:input wire:model="email" /><flux:error name="email" /></flux:field>
```

**Implementation:** Compose `flux:label`, the control, `flux:description`, and `flux:error`; shorthand props on controls are also supported.

**Current source:** [Flux UI](https://fluxui.dev/components/field.md).
