# Input

- **Availability:** Flux (free).
- **Use:** Collect short text and other native input values.
- **Main tags:** `flux:input`, `flux:input.group`, `flux:input.group.prefix`, `flux:input.group.suffix`.

**Starter:**

```blade
<flux:input wire:model="email" type="email" label="Email" />
```

## How to customize

- Choose the native input type and bind the value to Livewire, with label and error handling.
- Masks, icons, prefixes, suffixes, and attached buttons support structured entry without replacing the input itself.
- Configure disabled, readonly, invalid, clearable, copyable, and revealable behavior based on the field purpose.

## Capabilities

- **Shorthand** — tags `flux:input`.
- **Class targeting** — tags `flux:input`; settings `input:class="font-mono"`.
- **Types** — tags `flux:input`.
- **File** — tags `flux:input`; settings `multiple`.
- **Smaller** — tags `flux:input`; settings `size="sm"`.
- **Disabled** — tags `flux:input`; settings `disabled`.
- **Readonly** — tags `flux:input`; settings `readonly`, `variant="filled"`.
- **Invalid** — tags `flux:input`; settings `invalid`.
- **Input masking** — tags `flux:input`; settings `mask="(999) 999-9999"`, `mask:dynamic="$money($input)"`.
- **Icons** — tags `flux:input`; settings `icon`, `icon:trailing`.
- **Icon buttons** — tags `flux:input`, `flux:button`; settings `size="sm"`, `variant="subtle"`, `icon`.
- **Clearable, copyable, and viewable inputs** — tags `flux:input`; settings `clearable`, `viewable`, `icon`, `readonly`, `copyable`.
- **Keyboard hint** — tags `flux:input`; settings `kbd`, `icon`.
- **As a button** — tags `flux:input`; settings `as="button"`, `icon`, `kbd`.
- **With buttons** — tags `flux:input.group`, `flux:input`, `flux:button`, `flux:select`, `flux:select.option`; settings `icon`.
- **Text prefixes and suffixes** — tags `flux:input.group`, `flux:input.group.prefix`, `flux:input`, `flux:input.group.suffix`.
- **Input group labels** — tags `flux:field`, `flux:label`, `flux:input.group`, `flux:input.group.prefix`, `flux:input`.

**Full page:** `references/source/components/input.md` (bundled) or [live](https://fluxui.dev/components/input.md). Read it for exact props, slots, and values.
