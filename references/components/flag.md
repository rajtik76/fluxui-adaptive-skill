# Flag

- **Availability:** Flux (free).
- **Use:** Render a country flag from a region code.
- **Main tags:** `flux:flag`.
- **Common props:** `country`, `src`, `alt`, `size`, `circle`.

**Starter:**

```blade
<flux:flag country="US" />
```

## How to customize

- Choose a built-in flag with a two-letter region code, then set size or circular cropping.
- Supply a custom source when the needed artwork is outside the built-in registry.
- Add appropriate alternative text, especially when a flag communicates information beyond decoration.

## Capabilities

- **Sizes** — tags `flux:flag`; settings `country="US"`, `size="xl"`, `size="lg"`, `size="md"`, `size="xs"`.
- **Circle** — tags `flux:flag`; settings `circle`, `country="US"`.
- **Registry** — Built-in flags follow the Unicode RGI set; use custom `src` for other artwork.
- **Country select** — tags `flux:select`, `flux:select.option`, `flux:flag`; settings `size="xs"`.
- **Currency select** — tags `flux:select`, `flux:select.option`, `flux:flag`; settings `size="xs"`.
- **Analytics card** — tags `flux:card`, `flux:heading`, `flux:text`, `flux:flag`; settings `size="md"`.
- **Custom flags** — tags `flux:flag`; settings `src`, `alt="California"`, `size="xl"`.
- **Accessibility** — tags `flux:flag`; settings `country="CA"`, `alt="Canada"`.

## Component API

- **`flux:flag`** — props: `country`, `src`, `alt`, `size`, `circle`.

**Implementation:** Set a two-letter `country` code; `size`, `circle`, or a custom `src` change the display.

**Current source:** [Flux UI](https://fluxui.dev/components/flag.md).
