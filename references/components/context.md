# Context menu

- **Availability:** Flux Pro.
- **Use:** Open a menu from a right-click target.
- **Main tags:** `flux:context`.
- **Common props:** `wire:model`, `position`, `gap`, `offset`, `target`, `detail`, `disabled`.

**Starter:**

```blade
<flux:context><div>Right-click here</div><flux:menu><flux:menu.item wire:click="edit">Edit</flux:menu.item></flux:menu></flux:context>
```

**Implementation:** Wrap the target and a `flux:menu` in `flux:context`. Positioning and open state can be configured.

**Current source:** [Flux UI](https://fluxui.dev/components/context.md).
