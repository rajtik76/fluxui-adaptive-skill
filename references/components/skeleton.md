# Skeleton

- **Availability:** Flux (free).
- **Use:** Reserve space while content loads.
- **Main tags:** `flux:skeleton`, `flux:skeleton.line`, `flux:skeleton.group`.
- **Common props:** `animate`.

**Starter:**

```blade
<flux:skeleton.group animate="shimmer"><flux:skeleton.line /></flux:skeleton.group>
```

## How to customize

- Match placeholder dimensions to the content that will appear so layout remains stable.
- Combine blocks and lines in a group for cards, tables, or charts.
- Choose an animation style only when it helps communicate loading.

## Capabilities

- **Line of text** — tags `flux:skeleton.group`, `flux:skeleton.line`; settings `animate="shimmer"`.
- **Animation** — tags `flux:skeleton`; settings `animate="shimmer"`, `animate="pulse"`.
- **Table** — tags `flux:skeleton.group`, `flux:table`, `flux:table.columns`, `flux:table.column`, `flux:table.rows`; settings `animate="shimmer"`.
- **Chart** — tags `flux:card`, `flux:text`, `flux:heading`, `flux:skeleton`; settings `size="xl"`, `size="lg"`, `animate="shimmer"`.

## Component API

- **`flux:skeleton`** — props: `animate` (values `shimmer`, `pulse`).
- **`flux:skeleton.line`** — props: `size` (values `base`, `lg`), `animate` (values `shimmer`, `pulse`).
- **`flux:skeleton.group`** — props: `animate` (values `shimmer`, `pulse`).

**Implementation:** Combine blocks or lines in `flux:skeleton.group`; pick animation and dimensions to match the eventual content.

**Current source:** [Flux UI](https://fluxui.dev/components/skeleton.md).
