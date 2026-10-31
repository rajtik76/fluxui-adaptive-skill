# Command palette

- **Availability:** Flux Pro.
- **Use:** Offer a searchable list of actions.
- **Main tags:** `flux:command`, `flux:command.input`, `flux:command.items`, `flux:command.item`.

**Starter:**

```blade
<flux:command><flux:command.input placeholder="Search" /><flux:command.items><flux:command.item wire:click="create">Create</flux:command.item></flux:command.items></flux:command>
```

**Implementation:** Compose input, items, and actionable items under `flux:command`. It can also appear inside a modal.

**Current source:** [Flux UI](https://fluxui.dev/components/command.md).
