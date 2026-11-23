# Text

- **Availability:** Flux (free).
- **Use:** Render regular copy and links with consistent styling.
- **Main tags:** `flux:text`, `flux:link`.

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

**Full page:** `references/source/components/text.md` (bundled) or [live](https://fluxui.dev/components/text.md). Read it for exact props, slots, and values.
