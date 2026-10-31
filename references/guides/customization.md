# Customization

Choose the smallest customization level that solves the design requirement.

1. **Local Tailwind classes:** Add classes to a component for width, spacing, or another local adjustment. Check where classes land on composite components.
2. **Resolve class conflicts:** When Flux and application utilities target the same CSS property, inspect precedence. Tailwind's important modifier is possible for a one off override, but repeated conflict is a signal for a more deliberate customization.
3. **Publish component views:** `php artisan flux:publish` copies chosen Blade views into `resources/views/flux` for project ownership. `--all` publishes all. Published views can be changed freely, but must be reviewed when Flux is updated.
4. **Global styles:** Flux elements expose `data-flux-*` attributes that can be targeted for application wide overrides.

Do not publish every component for a small styling change. If the project already has published views, inspect them before relying on upstream examples.

**Current source:** [Flux UI customization](https://fluxui.dev/docs/customization.md).
