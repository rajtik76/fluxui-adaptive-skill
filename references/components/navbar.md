# Navbar

- **Availability:** Flux (free).
- **Use:** Build horizontal navigation or a related side navigation list.
- **Main tags:** `flux:navbar`, `flux:navbar.item`, `flux:navlist`, `flux:navlist.item`, `flux:navlist.group`.

**Starter:**

```blade
<flux:navbar><flux:navbar.item href="/">Home</flux:navbar.item></flux:navbar>
```

## How to customize

- Use navbar items for horizontal application navigation and mark the active destination.
- Icons, badges, and dropdowns can enrich items without hiding the main routes.
- Use navlist groups and collapsible sections for sidebar navigation.

## Capabilities

- **Detecting the current page** — tags `flux:navbar.item`; settings `current`.
- **With icons** — tags `flux:navbar`, `flux:navbar.item`; settings `icon`.
- **With badges** — tags `flux:navbar`, `flux:navbar.item`; settings `badge`, `badge:color="lime"`.
- **Dropdown navigation** — tags `flux:navbar`, `flux:navbar.item`, `flux:dropdown`, `flux:navmenu`, `flux:navmenu.item`; settings `icon:trailing`.
- **Navlist (sidebar)** — tags `flux:navlist`, `flux:navlist.item`; settings `icon`.
- **Navlist group** — tags `flux:navlist`, `flux:navlist.group`, `flux:navlist.item`; settings `heading`.
- **Collapsible groups** — tags `flux:navlist`, `flux:navlist.item`, `flux:navlist.group`; settings `icon`, `heading`, `expandable`.
- **Navlist badges** — tags `flux:navlist`, `flux:navlist.item`; settings `icon`, `badge`, `badge:color="lime"`.

## Component API

- **`flux:navbar.item`** — props: `href`, `current`, `icon`, `icon:trailing`, `badge`, `badge:color` (values `color`), `badge:variant` (values `solid`, `outline`; default `solid`).
- **`flux:navlist.item`** — props: `href`, `current`, `icon`, `badge`, `badge:color` (values `color`), `badge:variant` (values `solid`, `outline`; default `solid`).
- **`flux:navlist.group`** — props: `heading`, `expandable`, `expanded`.

**Implementation:** Place `flux:navbar.item` links in a navbar. Use the navlist family for sidebar menus and mark the active route.

**Current source:** [Flux UI](https://fluxui.dev/components/navbar.md).
