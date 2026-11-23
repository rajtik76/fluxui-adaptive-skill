# Dropdown

- **Availability:** Flux (free).
- **Use:** Attach a menu to a trigger.
- **Main tags:** `flux:dropdown`, `flux:menu`, `flux:menu.item`, `flux:menu.submenu`, `flux:menu.separator`, `flux:menu.checkbox.group`.

**Starter:**

```blade
<flux:dropdown><flux:button>Options</flux:button><flux:menu><flux:menu.item wire:click="edit">Edit</flux:menu.item></flux:menu></flux:dropdown>
```

## How to customize

- Place one trigger before the menu within the dropdown container.
- Menus support navigation, action items, checkbox/radio choices, groups, and nested submenus.
- Tune position, alignment, gap, offset, keyboard hints, and whether a choice keeps the menu open.

## Capabilities

- **Navigation menus** — tags `flux:dropdown`, `flux:profile`, `flux:navmenu`, `flux:navmenu.item`; settings `position="bottom"`, `align="end"`, `icon`.
- **Positioning** — tags `flux:dropdown`; settings `position="top"`, `align="start"`, `position="right"`, `align="center"`, `position="bottom"`, `position="left"`.
- **Offset & gap** — tags `flux:dropdown`; settings `offset="-15"`, `gap="2"`.
- **Keyboard hints** — tags `flux:dropdown`, `flux:button`, `flux:menu`, `flux:menu.item`; settings `icon:trailing`, `icon`, `kbd`, `variant="danger"`.
- **Checkbox items** — tags `flux:dropdown`, `flux:button`, `flux:menu`, `flux:menu.checkbox`; settings `icon:trailing`, `checked`.
- **Radio items** — tags `flux:dropdown`, `flux:button`, `flux:menu`, `flux:menu.radio.group`, `flux:menu.radio`; settings `icon:trailing`, `checked`.
- **Groups** — tags `flux:dropdown`, `flux:button`, `flux:menu`, `flux:menu.item`, `flux:menu.separator`; settings `icon:trailing`, `variant="danger"`.
- **Groups with headings** — tags `flux:dropdown`, `flux:button`, `flux:menu`, `flux:menu.group`, `flux:menu.item`; settings `icon:trailing`, `heading`.
- **Submenus** — tags `flux:dropdown`, `flux:button`, `flux:menu`, `flux:menu.submenu`, `flux:menu.radio`; settings `icon:trailing`, `heading`, `checked`, `variant="danger"`.
- **Keep open** — tags `flux:dropdown`, `flux:button`, `flux:menu`, `flux:menu.checkbox`; settings `icon:trailing`, `keep-open`, `checked`.

**Full page:** `references/source/components/dropdown.md` (bundled) or [live](https://fluxui.dev/components/dropdown.md). Read it for exact props, slots, and values.
