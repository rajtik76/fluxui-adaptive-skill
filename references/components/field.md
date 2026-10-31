# Field

- **Availability:** Flux (free).
- **Use:** Keep a form control, label, help text, and validation error together.
- **Main tags:** `flux:field`, `flux:label`, `flux:description`, `flux:error`, `flux:fieldset`, `flux:legend`.
- **Common props:** `variant`.

**Starter:**

```blade
<flux:field><flux:label>Email</flux:label><flux:input wire:model="email" /><flux:error name="email" /></flux:field>
```

## How to customize

- Group a label, control, description, and validation error under one field container.
- Shorthand props on common controls reduce markup; use the explicit structure when layout needs more control.
- Trailing descriptions, badges, split layouts, and fieldsets handle denser or grouped forms.

## Capabilities

- **Shorthand props** — tags `flux:input`.
- **With trailing description** — tags `flux:field`, `flux:label`, `flux:input`, `flux:error`, `flux:description`.
- **With badge** — tags `flux:field`, `flux:label`, `flux:input`, `flux:error`; settings `badge`.
- **Split layout** — tags `flux:input`.
- **Fieldset** — tags `flux:fieldset`, `flux:legend`, `flux:input`, `flux:select`.

## Component API

- **`flux:field`** — props: `variant` (values `block`, `inline`; default `block`).
- **`flux:label`** — props: `badge`; slots: `trailing`.
- **`flux:error`** — props: `name`, `message`, `bag` (default `default`), `deep` (default `true`), `icon` (default `exclamation-triangle`).
- **`flux:fieldset`** — props: `legend`, `description`.

**Implementation:** Compose `flux:label`, the control, `flux:description`, and `flux:error`; shorthand props on controls are also supported.

**Current source:** [Flux UI](https://fluxui.dev/components/field.md).
