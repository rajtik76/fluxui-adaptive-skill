# Breadcrumbs

- **Availability:** Flux (free).
- **Use:** Show the current page within a navigation hierarchy.
- **Main tags:** `flux:breadcrumbs`, `flux:breadcrumbs.item`.

**Starter:**

```blade
<flux:breadcrumbs><flux:breadcrumbs.item href="/">Home</flux:breadcrumbs.item><flux:breadcrumbs.item>Settings</flux:breadcrumbs.item></flux:breadcrumbs>
```

## How to customize

- Represent each ancestor as a linked item and leave the current location identifiable.
- Switch separator styling or add icons when that aids orientation.
- Collapse long paths with an ellipsis, optionally opening the hidden ancestors in a dropdown.

## Capabilities

- **With slashes** — tags `flux:breadcrumbs`, `flux:breadcrumbs.item`; settings `separator="slash"`.
- **With icon** — tags `flux:breadcrumbs`, `flux:breadcrumbs.item`; settings `icon`.
- **With ellipsis** — tags `flux:breadcrumbs`, `flux:breadcrumbs.item`; settings `icon`.
- **With ellipsis dropdown** — tags `flux:breadcrumbs`, `flux:breadcrumbs.item`, `flux:dropdown`, `flux:button`, `flux:navmenu`; settings `icon`.

## Component API

- **`flux:breadcrumbs.item`** — props: `href`, `icon`, `icon:variant` (values `outline`, `solid`, `mini`, `micro`; default `mini`), `separator` (default `chevron-right`).

**Implementation:** Nest `flux:breadcrumbs.item` elements with `href` for ancestors. Long trails can use an ellipsis and dropdown.

**Current source:** [Flux UI](https://fluxui.dev/components/breadcrumbs.md).
