# Kanban

- **Availability:** Flux Pro.
- **Use:** Arrange work cards into named columns.
- **Main tags:** `flux:kanban`, `flux:kanban.column`, `flux:kanban.column.header`, `flux:kanban.column.cards`, `flux:kanban.column.footer`, `flux:kanban.card`.

**Starter:**

```blade
<flux:kanban><flux:kanban.column><flux:kanban.column.header heading="Todo" /><flux:kanban.column.cards><flux:kanban.card heading="Task" /></flux:kanban.column.cards></flux:kanban.column></flux:kanban>
```

## How to customize

- Build each column from a header, card list, and optional footer; cards can have heading and extra content.
- Column actions and subheadings support workflow metadata.
- Render a card as a button when selecting it is an action; application state still owns the board data.

## Capabilities

- **Column actions** — tags `flux:kanban.column`, `flux:kanban.column.header`, `flux:dropdown`, `flux:button`, `flux:menu`.
- **Column subheading** — tags `flux:kanban.column`, `flux:kanban.column.header`, `flux:kanban.column.cards`; settings `heading`, `subheading="Ideas and suggestions"`.
- **Column footer** — tags `flux:kanban.column`, `flux:kanban.column.header`, `flux:kanban.column.cards`, `flux:kanban.column.footer`, `flux:kanban.card`; settings `count="5"`.
- **Card as button** — tags `flux:kanban.card`; settings `as="button"`, `heading`.
- **Card header** — tags `flux:kanban.card`, `flux:badge`; settings `as="button"`, `heading`.
- **Card footer** — tags `flux:kanban.card`, `flux:icon`, `flux:avatar.group`, `flux:avatar`; settings `as="button"`, `heading`.

**Full page:** `references/source/components/kanban.md` (bundled) or [live](https://fluxui.dev/components/kanban.md). Read it for exact props, slots, and values.
