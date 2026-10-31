# Heading

- **Availability:** Flux (free).
- **Use:** Give sections consistent heading typography.
- **Main tags:** `flux:heading`, `flux:text`.
- **Common props:** `size`, `level`, `accent`.

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

## Component API

- **`flux:heading`** — props: `size` (values `base`, `lg`, `xl`, `2xl`; default `base`), `level` (values `1`, `2`, `3`, `4`; default `div`), `accent`.
- **`flux:text`** — props: `size` (values `sm`, `base`, `lg`, `xl`; default `base`).

**Implementation:** Set visual `size` separately from semantic heading `level` so the document outline stays correct.

**Current source:** [Flux UI](https://fluxui.dev/components/heading.md).
