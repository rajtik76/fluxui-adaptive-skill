# Color picker

- **Availability:** Flux Pro.
- **Use:** Let someone choose or enter a color.
- **Main tags:** `flux:color-picker`, `flux:color-picker.area`, `flux:color-picker.slider`, `flux:color-picker.input`, `flux:color-picker.swatches`, `flux:color-picker.swatch`.
- **Common props:** `wire:model`, `value`, `name`, `format`, `type`, `placeholder`, `size`, `:swatches`, `dropper`, `clearable`, `copyable`, `label`.

**Starter:**

```blade
<flux:color-picker wire:model="themeColor" />
```

**Implementation:** Bind the selected color with Livewire. `format` controls formats such as hex or RGB; swatches, alpha, eyedropper, and clear controls are available.

**Current source:** [Flux UI](https://fluxui.dev/components/color-picker.md).
