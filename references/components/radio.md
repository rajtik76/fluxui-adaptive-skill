# Radio

- **Availability:** Flux (free).
- **Use:** Choose exactly one option in a group.
- **Main tags:** `flux:radio.group`, `flux:radio`, `flux:radio.indicator`.
- **Common props:** `wire:model`, `label`, `description`, `variant`, `invalid`.

**Starter:**

```blade
<flux:radio.group wire:model="plan" label="Plan"><flux:radio value="basic" label="Basic" /><flux:radio value="pro" label="Pro" /></flux:radio.group>
```

**Implementation:** Put `flux:radio` choices in `flux:radio.group` and bind the group. Segmented and card presentations are available.

**Current source:** [Flux UI](https://fluxui.dev/components/radio.md).
