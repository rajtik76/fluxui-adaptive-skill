# Command palette

- **Availability:** Flux Pro.
- **Use:** Offer a searchable list of actions.
- **Main tags:** `flux:command`, `flux:command.input`, `flux:command.items`, `flux:command.item`.

**Starter:**

```blade
<flux:command><flux:command.input placeholder="Search" /><flux:command.items><flux:command.item wire:click="create">Create</flux:command.item></flux:command.items></flux:command>
```

## How to customize

- Build the palette from a search input, item container, and actionable items.
- Each item can carry an icon, keyboard hint, and Livewire action.
- Place the palette in a modal when it should be invoked over the current page.

## Capabilities

- **As a modal** — tags `flux:modal.trigger`, `flux:input`, `flux:modal`, `flux:command`, `flux:command.input`; settings `icon`, `kbd`, `closable`.

**Full page:** `references/source/components/command.md` (bundled) or [live](https://fluxui.dev/components/command.md). Read it for exact props, slots, and values.
