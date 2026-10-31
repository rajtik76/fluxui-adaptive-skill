# Radio

- **Availability:** Flux (free).
- **Use:** Choose exactly one option in a group.
- **Main tags:** `flux:radio.group`, `flux:radio`, `flux:radio.indicator`.
- **Common props:** `wire:model`, `label`, `description`, `variant`, `invalid`.

**Starter:**

```blade
<flux:radio.group wire:model="plan" label="Plan"><flux:radio value="basic" label="Basic" /><flux:radio value="pro" label="Pro" /></flux:radio.group>
```

## How to customize

- Bind one selected value through a radio group and give each option a distinct value.
- Descriptions and fieldsets clarify longer choices.
- Segmented, card, pill, and button variants can change presentation while keeping single-choice behavior.

## Capabilities

- **With descriptions** — tags `flux:radio.group`, `flux:radio`; settings `checked`.
- **Within fieldset** — tags `flux:fieldset`, `flux:legend`, `flux:radio.group`, `flux:radio`; settings `checked`.
- **Segmented** — tags `flux:radio.group`, `flux:radio`; settings `variant="segmented"`.
- **Segmented with icons** — tags `flux:radio.group`, `flux:radio`; settings `variant="segmented"`, `icon`.
- **Radio cards** — tags `flux:radio.group`, `flux:radio`; settings `variant="cards"`, `checked`.
- **Vertical cards** — tags `flux:radio.group`, `flux:radio`; settings `variant="cards"`.
- **Cards with icons** — tags `flux:radio.group`, `flux:radio`; settings `variant="cards"`, `icon`.
- **Cards without indicators** — tags `flux:radio.group`, `flux:radio`; settings `variant="cards"`, `icon`.
- **Custom card content** — tags `flux:radio.group`, `flux:radio`, `flux:radio.indicator`, `flux:heading`, `flux:text`; settings `variant="cards"`, `checked`.
- **Pills** — tags `flux:radio.group`, `flux:radio`; settings `variant="pills"`.
- **Buttons** — tags `flux:radio.group`, `flux:radio`; settings `variant="buttons"`, `icon`, `checked`.

## Component API

- **`flux:radio.group`** — props: `wire:model`, `label`, `description`, `variant` (values `default`, `segmented`, `cards`, `pills`, `buttons`), `invalid`.
- **`flux:radio`** — props: `label`, `description`, `value`, `checked`, `disabled`, `icon`.

**Implementation:** Put `flux:radio` choices in `flux:radio.group` and bind the group. Segmented and card presentations are available.

**Current source:** [Flux UI](https://fluxui.dev/components/radio.md).
