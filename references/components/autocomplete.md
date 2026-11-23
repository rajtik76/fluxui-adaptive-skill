# Autocomplete

- **Availability:** Flux Pro.
- **Use:** Suggest matching values while someone types in a form field.
- **Main tags:** `flux:autocomplete`, `flux:autocomplete.item`.

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

**Full page:** `references/source/components/autocomplete.md` (bundled) or [live](https://fluxui.dev/components/autocomplete.md). Read it for exact props, slots, and values.
