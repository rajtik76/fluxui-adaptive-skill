# Avatar

- **Availability:** Flux (free).
- **Use:** Represent a person or entity with an image, initials, or icon.
- **Main tags:** `flux:avatar`, `flux:avatar.group`.

**Starter:**

```blade
<flux:avatar name="Ada Lovelace" />
```

## How to customize

- Choose an image source, initials, a name that generates initials, or an icon as the visible identity.
- Size, color, circular shape, badge, and tooltip options adapt the avatar to lists or profile views.
- Group avatars for overlapping collections; an avatar can also render as a button or link.

## Capabilities

- **Tooltip** — tags `flux:avatar`; settings `tooltip="Caleb Porzio"`, `src`, `tooltip`.
- **Initials** — tags `flux:avatar`; settings `initials="CP"`.
- **Size** — tags `flux:avatar`; settings `size="xl"`, `src`, `size="lg"`, `size="sm"`, `size="xs"`.
- **Icon** — tags `flux:avatar`; settings `icon`.
- **Colors** — tags `flux:avatar`; settings `color="red"`, `color="orange"`, `color="amber"`, `color="yellow"`, `color="lime"`, `color="green"`.
- **Auto color** — tags `flux:avatar`; settings `color="auto"`, `color:seed`.
- **Circle** — tags `flux:avatar`; settings `circle`, `src`.
- **Badge** — tags `flux:avatar`; settings `badge`, `badge:color="green"`, `src`, `badge:color="zinc"`, `badge:position="top right"`, `badge:circle`.
- **Groups** — tags `flux:avatar.group`, `flux:avatar`; settings `src`, `circle`.
- **As button** — tags `flux:avatar`; settings `as="button"`, `src`.
- **As link** — tags `flux:avatar`; settings `src`.
- **Testimonial** — tags `flux:icon.star`, `flux:heading`, `flux:avatar`, `flux:text`; settings `size="xl"`, `size="lg"`, `src`.
- **Grouped feature** — tags `flux:heading`, `flux:badge`, `flux:text`, `flux:avatar.group`, `flux:avatar`; settings `size="xl"`, `circle`, `size="lg"`, `src`.
- **Members table** — tags `flux:heading`, `flux:button`, `flux:table`, `flux:table.rows`, `flux:table.row`; settings `size="lg"`, `size="sm"`, `icon`, `circle`, `src`, `color="blue"`.
- **Assignees list** — tags `flux:card`, `flux:heading`, `flux:button`, `flux:separator`, `flux:avatar`; settings `size="sm"`, `icon`, `size="xs"`, `src`.
- **Select options** — tags `flux:select`, `flux:select.option`, `flux:avatar`; settings `circle`, `size="xs"`, `src`.
- **User popover** — tags `flux:dropdown`, `flux:avatar`, `flux:popover`, `flux:button`, `flux:heading`; settings `as="button"`, `src`, `icon`, `size="sm"`, `size="xl"`.

**Full page:** `references/source/components/avatar.md` (bundled) or [live](https://fluxui.dev/components/avatar.md). Read it for exact props, slots, and values.
