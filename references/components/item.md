# Item

- **Availability:** Flux (free).
- **Use:** A row with a heading, a line of supporting text, and a control at the end. Group items together for settings pages, account details, and lists of people or connections.
- **Main tags:** `flux:item.group`, `flux:item`, `flux:item.media`, `flux:item.heading`, `flux:item.subheading`, `flux:item.actions`.

**Starter:**

```blade
<flux:item>
    <flux:item.heading>Sign out</flux:item.heading>
    <flux:item.subheading>Your boards stay on this device.</flux:item.subheading>

    <flux:item.actions>
        <flux:button size="sm">Sign out</flux:button>
    </flux:item.actions>
</flux:item>
```

## How to customize

- Wrap rows in `flux:item.group` for one bordered surface with rules between items; a lone `flux:item` draws its own surface.
- Drop `flux:item.subheading` for a single-line row; lead with an avatar or icon in `flux:item.media`, end with buttons, a switch, a value, or a menu in `flux:item.actions`.
- Rows adapt to the item's own width, not the screen: a labeled button moves under the text, so the same markup works in a modal or sidebar.

## Capabilities

- **Single item** — tags `flux:item`, `flux:item.heading`, `flux:item.subheading`, `flux:item.actions`, `flux:button`; settings `size="sm"`.
- **Without a subheading** — tags `flux:item.group`, `flux:item`, `flux:item.heading`, `flux:item.actions`, `flux:text`, `flux:switch`; settings `aria-label`, `checked`.
- **Actions** — tags `flux:item.group`, `flux:item`, `flux:item.heading`, `flux:item.subheading`, `flux:item.actions`, `flux:button`, `flux:switch`, `flux:heading`; settings `size="sm"`, `variant="subtle"`, `aria-label`, `checked`.
- **Media** — tags `flux:item.group`, `flux:item`, `flux:item.media`, `flux:avatar`, `flux:item.heading`, `flux:item.subheading`; settings `size="sm"`, `circle`, `src`, `icon`, `initials`.
- **Narrow widths** — tags `flux:item`, `flux:item.media`, `flux:avatar`, `flux:item.heading`, `flux:item.subheading`, `flux:item.actions`, `flux:button`, `flux:item.group`, `flux:switch`; settings `circle`, `src`, `size="sm"`, `icon:trailing`, `variant="subtle"`, `aria-label`.
- **Examples** — team members with role menus, connected apps, billing, teams, notification switches, and a danger zone; tags `flux:dropdown`, `flux:menu.radio.group`, `flux:badge`, `flux:switch`.

**Full page:** `references/source/components/item.md` (bundled) or [live](https://fluxui.dev/components/item.md). Read it for exact props, slots, and values.
