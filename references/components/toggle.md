# Toggle

- **Availability:** Flux (free).
- **Use:** Offer a compact button-style boolean control.
- **Main tags:** `flux:toggle`.
- **Common props:** `wire:model`, `icon`, `on:icon`, `off:icon`, `label`, `on:label`, `off:label`, `size`, `variant`, `color`, `tooltip`, `checked`.

**Starter:**

```blade
<flux:toggle wire:model="enabled" icon="bolt" tooltip="Fast mode" />
```

## How to customize

- Bind a boolean value to a compact button-style setting.
- Customize size, variant, color, label, and icon; on/off states can each have distinct content.
- Use a change handler when the new value should be persisted immediately.

## Capabilities

- **Saving changes** — tags `flux:toggle`; settings `icon`, `tooltip="Active project"`.
- **Sizes** — tags `flux:toggle`; settings `icon`, `size="sm"`, `size="xs"`.
- **Variants** — tags `flux:toggle`; settings `icon`, `variant="filled"`, `variant="ghost"`, `variant="subtle"`.
- **Color** — tags `flux:toggle`; settings `icon`, `color="blue"`, `checked`, `color="red"`, `color="amber"`.
- **With label** — tags `flux:toggle`; settings `icon`.
- **Stateful icon** — tags `flux:toggle`; settings `on:icon="speaker-wave"`, `off:icon="speaker-x-mark"`, `tooltip="Toggle sound"`.
- **Custom icons** — tags `flux:toggle`, `flux:icon.shrink`, `flux:icon.expand`; settings `tooltip="Toggle fullscreen"`.
- **Stateful label** — tags `flux:toggle`; settings `on:label="Sound on"`, `off:label="Sound off"`.

## Component API

- **`flux:toggle`** — props: `wire:model`, `icon`, `on:icon`, `off:icon`, `label`, `on:label`, `off:label`, `size` (values `base`, `sm`, `xs`), `variant` (values `outline`, `filled`, `ghost`, `subtle`), `color`, `tooltip`, `checked`, `disabled`; slots: `icon`.

**Implementation:** Bind with Livewire. Icons and labels can differ by on/off state; `wire:change` can save a setting after a toggle.

**Current source:** [Flux UI](https://fluxui.dev/components/toggle.md).
