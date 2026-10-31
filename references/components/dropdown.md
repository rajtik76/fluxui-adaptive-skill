# Dropdown

- **Availability:** Flux (free).
- **Use:** Attach a menu to a trigger.
- **Main tags:** `flux:dropdown`, `flux:menu`, `flux:menu.item`, `flux:menu.submenu`, `flux:menu.separator`, `flux:menu.checkbox.group`.
- **Common props:** `position`, `align`, `offset`, `gap`.

**Starter:**

```blade
<flux:dropdown><flux:button>Options</flux:button><flux:menu><flux:menu.item wire:click="edit">Edit</flux:menu.item></flux:menu></flux:dropdown>
```

**Implementation:** Put a trigger and `flux:menu` in `flux:dropdown`. Menu items can navigate or run actions; nested menus and choice items are available.

**Current source:** [Flux UI](https://fluxui.dev/components/dropdown.md).
