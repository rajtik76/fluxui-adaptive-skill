# Autocomplete

- **Availability:** Flux Pro.
- **Use:** Suggest matching values while someone types in a form field.
- **Main tags:** `flux:autocomplete`, `flux:autocomplete.item`.
- **Common props:** `wire:model`, `type`, `label`, `description`, `placeholder`, `size`, `variant`, `disabled`, `readonly`, `invalid`, `multiple`, `mask`.

**Starter:**

```blade
<flux:autocomplete wire:model="state" label="State"><flux:autocomplete.item>Alabama</flux:autocomplete.item></flux:autocomplete>
```

**Implementation:** Bind the field with `wire:model` and put `flux:autocomplete.item` choices inside. It also supports multiple selections.

**Current source:** [Flux UI](https://fluxui.dev/components/autocomplete.md).
