# Checkbox

- **Availability:** Flux (free).
- **Use:** Collect one or more boolean choices.
- **Main tags:** `flux:checkbox`, `flux:checkbox.group`, `flux:checkbox.all`.
- **Common props:** `wire:model`, `label`, `description`, `value`, `checked`, `indeterminate`, `disabled`, `invalid`.

**Starter:**

```blade
<flux:checkbox wire:model="accepted" label="Accept terms" />
```

## How to customize

- Bind one boolean choice directly or group several values under a common label.
- Descriptions and fieldsets explain choices; checked, disabled, and select-all states handle common forms.
- Card, pill, and button presentations change appearance while preserving checkbox selection semantics.

## Capabilities

- **Checkbox group** — tags `flux:checkbox.group`, `flux:checkbox`; settings `checked`.
- **With descriptions** — tags `flux:checkbox.group`, `flux:checkbox`; settings `checked`.
- **Horizontal fieldset** — tags `flux:fieldset`, `flux:legend`, `flux:description`, `flux:checkbox`; settings `checked`.
- **Check-all** — tags `flux:checkbox.group`, `flux:checkbox.all`, `flux:checkbox`; settings `checked`.
- **Checked** — tags `flux:checkbox`; settings `checked`.
- **Disabled** — tags `flux:checkbox`; settings `disabled`.
- **Checkbox cards** — tags `flux:checkbox.group`, `flux:checkbox`; settings `variant="cards"`, `checked`.
- **Vertical cards** — tags `flux:checkbox.group`, `flux:checkbox`; settings `variant="cards"`, `checked`.
- **Cards with icons** — tags `flux:checkbox.group`, `flux:checkbox`; settings `variant="cards"`, `checked`.
- **Custom card content** — tags `flux:checkbox.group`, `flux:checkbox`, `flux:checkbox.indicator`, `flux:heading`, `flux:text`; settings `variant="cards"`, `checked`.
- **Pills** — tags `flux:checkbox.group`, `flux:checkbox`; settings `variant="pills"`.
- **Buttons** — tags `flux:checkbox.group`, `flux:checkbox`; settings `variant="buttons"`.

## Component API

- **`flux:checkbox`** — props: `wire:model`, `label`, `description`, `value`, `checked`, `indeterminate`, `disabled`, `invalid`.
- **`flux:checkbox.group`** — props: `wire:model`, `label`, `description`, `variant` (values `default`, `cards`, `pills`, `buttons`), `disabled`, `invalid`.
- **`flux:checkbox.all`** — props: `label`, `description`, `disabled`.

**Implementation:** Bind a single checkbox or a checkbox group with Livewire. Use `value` for grouped options; `flux:checkbox.all` supports select-all behavior.

**Current source:** [Flux UI](https://fluxui.dev/components/checkbox.md).
