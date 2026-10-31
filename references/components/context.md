# Context menu

- **Availability:** Flux Pro.
- **Use:** Open a menu from a right-click target.
- **Main tags:** `flux:context`.
- **Common props:** `wire:model`, `position`, `gap`, `offset`, `target`, `detail`, `disabled`.

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

## Component API

- **`flux:context`** — props: `wire:model`, `position`, `gap` (default `4`), `offset`, `target`, `detail`, `disabled`.

**Implementation:** Wrap the target and a `flux:menu` in `flux:context`. Positioning and open state can be configured.

**Current source:** [Flux UI](https://fluxui.dev/components/context.md).
