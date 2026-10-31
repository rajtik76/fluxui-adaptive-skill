# Accordion

- **Availability:** Flux Pro.
- **Use:** Show expandable sections such as FAQs.
- **Main tags:** `flux:accordion`, `flux:accordion.item`, `flux:accordion.heading`, `flux:accordion.content`.
- **Common props:** `variant`, `transition`, `exclusive`.

**Starter:**

```blade
<flux:accordion><flux:accordion.item heading="Question">Answer</flux:accordion.item></flux:accordion>
```

## How to customize

- Compose each item with separate heading and content tags, or use the item heading shorthand for simple text.
- The container controls animated expansion and whether opening one item closes another. Individual items can begin open or be disabled.
- Collapsed text remains searchable through the browser find command; a matching item opens without an extra attribute.

## Capabilities

- **Shorthand** — An item may put its title in `heading`; otherwise compose separate heading and content children.
- **With transition** — Set `transition` on the container to animate expansion and collapse.
- **Findable content** — Collapsed content can be found with the browser page search; Flux opens the matching item automatically. No prop is needed.
- **Disabled** — Set `disabled` on an item to prevent interaction.
- **Exclusive** — Set `exclusive` on the container to keep only one item open.
- **Expanded** — Set `expanded` on an item to make it open initially.
- **Leading icon** — Use `variant="reverse"` on the container to place the icon before the heading.

## Component API

- **`flux:accordion`** — props: `variant`, `transition` (default `false`), `exclusive` (default `false`).
- **`flux:accordion.item`** — props: `heading`, `expanded` (default `false`), `disabled` (default `false`).

**Implementation:** Place item, heading, and content tags inside the accordion. Use `exclusive` for one open item at a time; items can start `expanded` or be `disabled`.

**Current source:** [Flux UI](https://fluxui.dev/components/accordion.md).
