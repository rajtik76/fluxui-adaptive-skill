# Color picker

- **Availability:** Flux Pro.
- **Use:** Let someone choose or enter a color.
- **Main tags:** `flux:color-picker`, `flux:color-picker.area`, `flux:color-picker.slider`, `flux:color-picker.input`, `flux:color-picker.swatches`, `flux:color-picker.swatch`.
- **Common props:** `wire:model`, `value`, `name`, `format`, `type`, `placeholder`, `size`, `:swatches`, `dropper`, `clearable`, `copyable`, `label`.

**Starter:**

```blade
<flux:color-picker wire:model="themeColor" />
```

## How to customize

- Bind the color value and choose its output format, including alpha-aware forms when transparency matters.
- Offer swatches, a color area, direct input, or an eyedropper depending on how precise selection must be.
- Customize trigger, size, layout, clear/copy controls, and disabled state for the surrounding form.

## Capabilities

- **Format** — tags `flux:color-picker`; settings `format="hex"`, `format="hexa"`, `format="rgb"`, `format="rgba"`, `format="hsl"`, `format="hsla"`.
- **Sizes** — tags `flux:color-picker`; settings `size="sm"`, `size="xs"`.
- **Button trigger** — tags `flux:color-picker`.
- **Custom swatches** — tags `flux:color-picker`.
- **No swatches** — tags `flux:color-picker`.
- **Custom layout** — tags `flux:color-picker`, `flux:color-picker.input`, `flux:separator`, `flux:color-picker.area`, `flux:color-picker.slider`; settings `channel="hue"`.
- **Dropper** — tags `flux:color-picker`; settings `dropper`.
- **Clearable** — tags `flux:color-picker`; settings `clearable`.
- **Copyable** — tags `flux:color-picker`; settings `copyable`.
- **Disabled** — tags `flux:color-picker`; settings `disabled`.

## Component API

- **`flux:color-picker`** — props: `wire:model`, `value`, `name`, `format` (values `hex`, `hexa`, `rgb`, `rgba`, `hsl`, `hsla`), `type` (values `input`, `button`), `placeholder`, `size` (values `sm`, `xs`), `:swatches`, `dropper` (default `false`), `clearable` (default `false`), `copyable` (default `false`), `label`, `description`, `disabled` (default `false`), `invalid`.
- **`flux:color-picker.area`** — props: `class`.
- **`flux:color-picker.slider`** — props: `channel` (values `hue`, `alpha`).
- **`flux:color-picker.input`** — props: `placeholder`.
- **`flux:color-picker.swatches`** — props: `class`.
- **`flux:color-picker.swatch`** — props: `value`, `label`.
- **`flux:color-picker.dropper`** — props: `class`.

**Implementation:** Bind the selected color with Livewire. `format` controls formats such as hex or RGB; swatches, alpha, eyedropper, and clear controls are available.

**Current source:** [Flux UI](https://fluxui.dev/components/color-picker.md).
