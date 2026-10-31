# Toggle

- **Availability:** Flux (free).
- **Use:** Offer a compact button-style boolean control.
- **Main tags:** `flux:toggle`.
- **Common props:** `wire:model`, `icon`, `on:icon`, `off:icon`, `label`, `on:label`, `off:label`, `size`, `variant`, `color`, `tooltip`, `checked`.

**Starter:**

```blade
<flux:toggle wire:model="enabled" icon="bolt" tooltip="Fast mode" />
```

**Implementation:** Bind with Livewire. Icons and labels can differ by on/off state; `wire:change` can save a setting after a toggle.

**Current source:** [Flux UI](https://fluxui.dev/components/toggle.md).
