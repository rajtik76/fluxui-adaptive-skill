# Context menu

- **Availability:** Flux Pro.
- **Use:** Open a menu from a right-click target.
- **Main tags:** `flux:context`.

**Starter:**

```blade
<flux:context><div>Right-click here</div><flux:menu><flux:menu.item wire:click="edit">Edit</flux:menu.item></flux:menu></flux:context>
```

## How to customize

- Wrap the interaction target and its menu so a right-click exposes contextual actions.
- Menu items can be ordinary actions or navigation just like dropdown menu items.
- Position, gap, offset, target detail, and bound open state control presentation.

## Capabilities

- **Context trigger** — Wrap the target and its menu so right-click opens the actions.
- **Placement and state** — Configure position, gap, offset, or bind the open state with Livewire.

**Full page:** `references/source/components/context.md` (bundled) or [live](https://fluxui.dev/components/context.md). Read it for exact props, slots, and values.
