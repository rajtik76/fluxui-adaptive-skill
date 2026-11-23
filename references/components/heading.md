# Heading

- **Availability:** Flux (free).
- **Use:** Give sections consistent heading typography.
- **Main tags:** `flux:heading`, `flux:text`.

**Starter:**

```blade
<flux:heading level="2" size="lg">Account</flux:heading>
```

## How to customize

- Set visual size for hierarchy while choosing the semantic heading level independently.
- Combine with regular text for an introduction or supporting description.
- Maintain a coherent document outline even if the visual size differs from the level.

## Capabilities

- **Sizes** — tags `flux:heading`; settings `size="lg"`, `size="xl"`, `size="2xl"`.
- **Heading level** — tags `flux:heading`, `flux:text`; settings `level="3"`.
- **Leading subheading** — tags `flux:text`, `flux:heading`, `flux:icon.arrow-trending-up`; settings `size="xl"`.

**Full page:** `references/source/components/heading.md` (bundled) or [live](https://fluxui.dev/components/heading.md). Read it for exact props, slots, and values.
