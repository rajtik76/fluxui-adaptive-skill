# Rich text editor

- **Availability:** Flux Pro.
- **Use:** Edit formatted text in a Livewire form.
- **Main tags:** `flux:editor`, `flux:editor.toolbar`, `flux:editor.button`, `flux:editor.content`.
- **Common props:** `wire:model`, `value`, `label`, `description`, `description:trailing`, `badge`, `placeholder`, `toolbar`, `disabled`, `invalid`.

**Starter:**

```blade
<flux:editor wire:model="content" label="Content" />
```

**Implementation:** Bind content with `wire:model`. The toolbar can be customized; confirm the expected stored format and validation in the live docs.

**Current source:** [Flux UI](https://fluxui.dev/components/editor.md).
