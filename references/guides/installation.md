# Installation

Use this guide when adding Flux to a Laravel application or diagnosing missing assets. The current guide covers Laravel, Livewire, and Tailwind version prerequisites; check the project's installed versions and the [live installation page](https://fluxui.dev/docs/installation.md) before changing dependencies.

## Application setup

1. Install the free package with `composer require livewire/flux`.
2. If the project has a Pro license, activate it with `php artisan flux:activate`. Composer authentication for the private package is separate from the public package.
3. Put `@fluxAppearance` in the document head and `@fluxScripts` near the end of the body alongside Livewire's scripts.
4. Import Tailwind and `../../vendor/livewire/flux/dist/flux.css` from `resources/css/app.css`. Configure the `dark` custom variant using the `.dark` ancestor selector.
5. An Inter font is optional; configure it through the app layout and Tailwind theme only if the project wants it.

## Operational details

- Pro credentials can be supplied through Composer authentication in a new checkout or CI environment. Keep license values in the environment's secret store; do not commit an `auth.json` containing credentials.
- Laravel Forge, Laravel Cloud, and GitHub Actions have separate credential setup paths. Read their live sections for the exact deployment environment.
- Published component views become project owned. Review Flux release notes before updating a project that published them.
- If Flux asset routes fail under a custom nginx configuration, check the routing guidance on the current installation page.

## Related guidance

Read [Theming](theming.md) for colors, [Dark mode](dark-mode.md) for appearance controls, and [Customization](customization.md) before publishing component views. For an existing v1 project, start with [Upgrade guide](upgrading.md).

**Full page:** `references/source/docs/installation.md` (bundled) or [live](https://fluxui.dev/docs/installation.md).
