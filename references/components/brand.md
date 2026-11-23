# Brand

- **Availability:** Flux (free).
- **Use:** Display a logo and product name in navigation or a header.
- **Main tags:** `flux:brand`.

**Starter:**

```blade
<flux:brand href="/" logo="/logo.svg" name="Acme" />
```

## How to customize

- Supply a name and logo path for ordinary header branding, with a destination when the brand should link home.
- Use the logo slot for custom markup or show only the logo when space is tight.
- Keep the logo alternative text meaningful when the visible name is omitted.

## Capabilities

- **Logo slot** — tags `flux:brand`, `flux:icon`.
- **Logo only** — tags `flux:brand`; settings `logo="/img/demo/logo.png"`.
- **Header with brand** — tags `flux:header`, `flux:brand`, `flux:navbar`, `flux:navbar.item`, `flux:spacer`.

**Full page:** `references/source/components/brand.md` (bundled) or [live](https://fluxui.dev/components/brand.md). Read it for exact props, slots, and values.
