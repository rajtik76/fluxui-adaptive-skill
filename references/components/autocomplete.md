# Autocomplete

- **Availability:** Flux Pro.
- **Use:** Suggest matching values while someone types in a form field.
- **Main tags:** `flux:autocomplete`, `flux:autocomplete.item`.
- **Common props:** `wire:model`, `type`, `label`, `description`, `placeholder`, `size`, `variant`, `disabled`, `readonly`, `invalid`, `multiple`, `mask`.

**Starter:**

```blade
<flux:autocomplete wire:model="state" label="State"><flux:autocomplete.item>Alabama</flux:autocomplete.item></flux:autocomplete>
```

## How to customize

- Bind the input to Livewire and supply selectable items; use labels and placeholder text like other form controls.
- Enable multiple selection when the property should hold more than one chosen value.
- Read the live reference for less common input props such as masks, icons, and validation behavior.

## Capabilities

- **Suggestions** — Place autocomplete items under the bound field to offer choices while typing.
- **Multiple values** — Enable `multiple` when the form should keep several selections.

## Component API

- **`flux:autocomplete`** — props: `wire:model`, `type` (default `text`), `label`, `description`, `placeholder`, `size` (values `sm`, `xs`), `variant` (values `filled`; default `outline`), `disabled`, `readonly`, `invalid`, `multiple`, `mask`, `icon`, `icon:trailing`, `kbd`, `clearable`, `copyable`, `viewable`, `as` (values `button`; default `input`), `container:class`, `input:class`; slots: `icon`, `icon:leading`, `icon:trailing`.
- **`flux:autocomplete.item`** — props: `disabled`.

**Implementation:** Bind the field with `wire:model` and put `flux:autocomplete.item` choices inside. It also supports multiple selections.

**Current source:** [Flux UI](https://fluxui.dev/components/autocomplete.md).
