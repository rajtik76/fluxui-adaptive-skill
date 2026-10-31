# Switch

- **Availability:** Flux (free).
- **Use:** Turn a boolean setting on or off.
- **Main tags:** `flux:switch`.
- **Common props:** `wire:model`, `label`, `description`, `align`, `disabled`.

**Starter:**

```blade
<flux:switch wire:model="enabled" label="Enable notifications" />
```

## How to customize

- Bind a boolean setting and provide a clear label describing the enabled state.
- Use a fieldset when switches form a group.
- Align the control to the left when that better matches the form layout.

## Capabilities

- **Fieldset** — tags `flux:fieldset`, `flux:legend`, `flux:switch`, `flux:separator`.
- **Left align** — tags `flux:fieldset`, `flux:legend`, `flux:switch`; settings `align="left"`.

## Component API

- **`flux:switch`** — props: `wire:model`, `label`, `description`, `align` (values `right|start`, `left|end`), `disabled`.

**Implementation:** Bind with Livewire and provide a clear label. Use an inline field or a fieldset for grouped settings.

**Current source:** [Flux UI](https://fluxui.dev/components/switch.md).
