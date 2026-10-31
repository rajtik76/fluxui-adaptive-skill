# Breadcrumbs

- **Availability:** Flux (free).
- **Use:** Show the current page within a navigation hierarchy.
- **Main tags:** `flux:breadcrumbs`, `flux:breadcrumbs.item`.

**Starter:**

```blade
<flux:breadcrumbs><flux:breadcrumbs.item href="/">Home</flux:breadcrumbs.item><flux:breadcrumbs.item>Settings</flux:breadcrumbs.item></flux:breadcrumbs>
```

**Implementation:** Nest `flux:breadcrumbs.item` elements with `href` for ancestors. Long trails can use an ellipsis and dropdown.

**Current source:** [Flux UI](https://fluxui.dev/components/breadcrumbs.md).
