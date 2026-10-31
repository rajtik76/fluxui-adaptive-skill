# Select

- **Availability:** Flux (free).
- **Use:** Choose from a controlled set of options.
- **Main tags:** `flux:select`, `flux:select.option`, `flux:select.group`, `flux:select.option.create`, `flux:select.option.empty`, `flux:select.button`.
- **Common props:** `wire:model`, `placeholder`, `label`, `description`, `description:trailing`, `badge`, `size`, `variant`, `multiple`, `filter`, `searchable`, `empty`.

**Starter:**

```blade
<flux:select wire:model="role" label="Role"><flux:select.option value="admin">Admin</flux:select.option></flux:select>
```

**Implementation:** Bind the select and add `flux:select.option` values. Native and custom variants differ; search, grouping, and multiple selection depend on the chosen variant.

**Current source:** [Flux UI](https://fluxui.dev/components/select.md).
