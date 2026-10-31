# Theming

Flux distinguishes a neutral **base palette** from an **accent palette** for prominent actions and interactive elements. Prefer project wide CSS variables over one off component color overrides when establishing an application theme.

## Base palette

Flux uses the `zinc` palette by default. To choose another neutral family, redefine the `--color-zinc-*` tokens in the application's Tailwind `@theme` block. Keep the complete shade scale coherent so text, borders, and surfaces still work in both appearances.

## Accent palette

Set `--color-accent`, `--color-accent-content`, and `--color-accent-foreground` in `@theme`; provide dark appearance values in a `.dark` rule under `@layer theme`. These tokens cover action backgrounds, readable accent text, and foreground text placed on an accent surface. Tailwind utilities can use the resulting accent colors.

Tabs, links, and navigation items may follow the accent by default. On supported elements, `:accent="false"` opts out and uses the base treatment. Check the individual component page before applying this prop elsewhere.

The [theme builder](https://fluxui.dev/themes) can help choose values, while [Customization](customization.md) covers component level changes.

**Current source:** [Flux UI theming](https://fluxui.dev/docs/theming.md).
