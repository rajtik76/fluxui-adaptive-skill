# Text

- **Availability:** Flux (free).
- **Use:** Render regular copy and links with consistent styling.
- **Main tags:** `flux:text`, `flux:link`.
- **Common props:** `size`, `variant`, `color`, `inline`.

**Starter:**

```blade
<flux:text>Body copy</flux:text>
```

## How to customize

- Use text for body copy and link for navigation with consistent default styling.
- Size and color variants adjust emphasis; link variants can resemble a button where appropriate.
- Keep heading hierarchy separate from body typography.

## Capabilities

- **Size** — tags `flux:text`.
- **Color** — tags `flux:text`; settings `variant="strong"`, `variant="subtle"`, `color="blue"`.
- **Link** — tags `flux:text`, `flux:link`.
- **Link variants** — tags `flux:link`; settings `variant="ghost"`, `variant="subtle"`.
- **Link as button** — tags `flux:link`; settings `as="button"`.

## Component API

- **`flux:text`** — props: `size` (values `sm`, `default`, `lg`, `xl`; default `default`), `variant` (values `strong`, `subtle`; default `default`), `color` (values `default`, `red`, `orange`, `yellow`, `lime`, `green`, `emerald`, `teal`, `cyan`, `sky`, `blue`, `indigo`; default `default`), `inline`.
- **`flux:link`** — props: `href`, `variant` (values `default`, `ghost`, `subtle`; default `default`), `external`, `as` (values `a`, `button`).

**Implementation:** Use `flux:text` for body copy and `flux:link` for navigation; set size or color only where hierarchy needs it.

**Current source:** [Flux UI](https://fluxui.dev/components/text.md).
