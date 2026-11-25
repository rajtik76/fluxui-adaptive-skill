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

- TODO: two or three bullets on how to adapt this component, written from the full page.

## Capabilities

- **Single item** — tags `flux:item`, `flux:item.heading`, `flux:item.subheading`, `flux:item.actions`, `flux:button`; settings `size="sm"`.
- **Without a subheading** — tags `flux:item.group`, `flux:item`, `flux:item.heading`, `flux:item.actions`, `flux:text`, `flux:switch`; settings `aria-label`, `checked`.
- **Actions** — tags `flux:item.group`, `flux:item`, `flux:item.heading`, `flux:item.subheading`, `flux:item.actions`, `flux:button`, `flux:switch`, `flux:heading`; settings `size="sm"`, `variant="subtle"`, `aria-label`, `checked`.
- **Media** — tags `flux:item.group`, `flux:item`, `flux:item.media`, `flux:avatar`, `flux:item.heading`, `flux:item.subheading`; settings `size="sm"`, `circle`, `src`, `icon`, `initials`.
- **Narrow widths** — tags `flux:item`, `flux:item.media`, `flux:avatar`, `flux:item.heading`, `flux:item.subheading`, `flux:item.actions`, `flux:button`, `flux:item.group`, `flux:switch`; settings `circle`, `src`, `size="sm"`, `icon:trailing`, `variant="subtle"`, `aria-label`.
- **Examples** — tags `flux:item.group`, `flux:item`, `flux:item.media`, `flux:avatar`, `flux:item.heading`, `flux:text`, `flux:item.subheading`, `flux:item.actions`, `flux:dropdown`, `flux:button`, `flux:menu`, `flux:menu.radio.group`, `flux:menu.radio`, `flux:menu.separator`, `flux:menu.item`, `flux:badge`, `flux:heading`, `flux:switch`; settings `size="sm"`, `circle`, `src`, `inline`, `variant="subtle"`, `align="end"`.

**Full page:** `references/source/components/item.md` (bundled) or [live](https://fluxui.dev/components/item.md). Read it for exact props, slots, and values.
