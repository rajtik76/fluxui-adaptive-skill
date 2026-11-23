# Patterns

Read this guide when a component prop, forwarded HTML attribute, Tailwind class, slot, or Livewire binding behaves unexpectedly. The same conventions recur across the component catalog.

## Props and attributes

- Flux props such as `variant` select internal behavior or classes. Other attributes may pass through to an underlying HTML element.
- User supplied Tailwind classes merge with component classes. When utilities conflict, check the rendered element and CSS precedence; a Tailwind important modifier can resolve a local override, but publishing a variant or using a global style may be cleaner for repeated changes.
- Composite controls can forward styling attributes to a wrapper and behavioral attributes to the actual input. Inspect the rendered markup when an attribute appears on the wrong element.

## Recurring component conventions

- `variant`, `size`, and `icon` are common but their accepted values are component specific. A trailing icon may use `icon:trailing`.
- Keyboard hints use `kbd` where supported. `inset` can adjust alignment through negative margin on supported components.
- Prefixes such as `icon:variant` forward settings into an internally rendered child. Use dynamic Blade props with `false` when opting out of a default behavior.
- Input components bind with `wire:model` like other Livewire controls. A `.group` wrapper often coordinates otherwise independent instances.
- Prefer explicit child components where they make composition clear; named slots exist for cases that require a custom trigger or region.

The guide also covers Blade attribute syntax edge cases. For an exact prop or slot, consult the selected component reference and current page.

**Full page:** `references/source/docs/patterns.md` (bundled) or [live](https://fluxui.dev/docs/patterns.md).
