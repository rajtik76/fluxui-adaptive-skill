# Switch

- **Availability:** Flux (free).
- **Use:** Turn a boolean setting on or off.
- **Main tags:** `flux:switch`.

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

**Full page:** `references/source/components/switch.md` (bundled) or [live](https://fluxui.dev/components/switch.md). Read it for exact props, slots, and values.
