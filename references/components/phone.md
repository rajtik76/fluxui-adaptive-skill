# Phone

- **Availability:** Flux Pro.
- **Use:** Collect an international telephone number.
- **Main tags:** `flux:phone`.
- **Common props:** `wire:model`, `value`, `name`, `country`, `countries`, `country-order`, `placeholder`, `size`, `variant`, `label`, `description`, `disabled`.

**Starter:**

```blade
<flux:phone wire:model="phone" country="US" label="Phone" />
```

**Implementation:** Bind with Livewire and set an initial `country` where known. Flux normalizes valid-looking values to E.164; still validate on the server.

**Current source:** [Flux UI](https://fluxui.dev/components/phone.md).
