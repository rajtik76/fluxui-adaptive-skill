# Kanban

- **Availability:** Flux Pro.
- **Use:** Arrange work cards into named columns.
- **Main tags:** `flux:kanban`, `flux:kanban.column`, `flux:kanban.column.header`, `flux:kanban.column.cards`, `flux:kanban.column.footer`, `flux:kanban.card`.

**Starter:**

```blade
<flux:kanban><flux:kanban.column><flux:kanban.column.header heading="Todo" /><flux:kanban.column.cards><flux:kanban.card heading="Task" /></flux:kanban.column.cards></flux:kanban.column></flux:kanban>
```

**Implementation:** Compose columns, column headers, card lists, and cards. Provide the underlying item data and actions from the application.

**Current source:** [Flux UI](https://fluxui.dev/components/kanban.md).
