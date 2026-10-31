# Dropdown

- **Availability:** Flux (free).
- **Use:** Attach a menu to a trigger.
- **Main tags:** `flux:dropdown`, `flux:menu`, `flux:menu.item`, `flux:menu.submenu`, `flux:menu.separator`, `flux:menu.checkbox.group`.
- **Common props:** `position`, `align`, `offset`, `gap`.

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

## Component API

- **`flux:dropdown`** — props: `position` (values `top`, `right`, `bottom`, `left`), `align` (values `start`, `center`, `end`; default `start`), `offset` (default `0`), `gap` (default `4`).
- **`flux:menu`** — props: `keep-open`.
- **`flux:menu.item`** — props: `icon`, `icon:trailing`, `icon:variant` (values `outline`, `solid`, `mini`, `micro`), `kbd`, `suffix`, `variant` (values `default`, `danger`), `disabled`, `keep-open`.
- **`flux:menu.submenu`** — props: `heading`, `icon`, `icon:trailing`, `icon:variant` (values `outline`, `solid`, `mini`, `micro`), `keep-open`.
- **`flux:menu.checkbox.group`** — props: `wire:model`.
- **`flux:menu.checkbox`** — props: `wire:model`, `checked`, `disabled`, `keep-open`.
- **`flux:menu.radio.group`** — props: `wire:model`, `keep-open`.
- **`flux:menu.radio`** — props: `checked`, `disabled`, `keep-open`.

**Implementation:** Put a trigger and `flux:menu` in `flux:dropdown`. Menu items can navigate or run actions; nested menus and choice items are available.

**Current source:** [Flux UI](https://fluxui.dev/components/dropdown.md).
