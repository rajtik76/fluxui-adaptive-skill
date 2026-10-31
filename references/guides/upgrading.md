# Upgrade guide

This page concerns migration from Flux v1 to v2. Inspect the installed Flux, Livewire, Laravel, and Tailwind versions first; apply migration steps only to a project that needs them.

## Migration map

- Update Flux packages to the v2 line with Composer and migrate the app to Tailwind CSS v4.
- Replace the removed `@fluxStyles` directive with a CSS import of Flux styles. `@fluxAppearance` manages the dark class; it is not a general replacement for CSS loading.
- Clear compiled Blade views with `php artisan view:clear` after the package update.
- Move accent palette and reassigned gray values from older Tailwind configuration to the v4 CSS theme and dark theme blocks.
- Review any previous `darkMode: null` configuration and decide whether the new layout should include `@fluxAppearance`.
- Rename old component tags in application views. The guide lists the affected select and table child tags; search the project before editing.

Published component views may need more work than ordinary app views because local copies do not receive upstream changes automatically. Compare them with the current Flux release notes.

**Current source:** [Flux UI upgrade guide](https://fluxui.dev/docs/upgrading.md).
