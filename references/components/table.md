# Table

- **Availability:** Flux (free).
- **Use:** Display rows and columns of structured data.
- **Main tags:** `flux:table`, `flux:table.columns`, `flux:table.column`, `flux:table.rows`, `flux:table.row`, `flux:table.cell`.

**Starter:**

```blade
<flux:table><flux:table.columns><flux:table.column>Name</flux:table.column></flux:table.columns><flux:table.rows><flux:table.row><flux:table.cell>Ada</flux:table.cell></flux:table.row></flux:table.rows></flux:table>
```

## How to customize

- Compose columns, rows, and cells from structured data rather than styling a plain table ad hoc.
- Add sortable column state and pagination when the dataset warrants them.
- Full-bleed layout and sticky headers or columns support dense scrolling tables.

## Capabilities

- **Simple** — tags `flux:table`, `flux:table.columns`, `flux:table.column`, `flux:table.rows`, `flux:table.row`; settings `variant="strong"`.
- **Full-bleed** — tags `flux:card`, `flux:heading`, `flux:text`, `flux:button`, `flux:table`; settings `bleed`, `container:class="mt-6"`, `align="end"`, `variant="strong"`.
- **Custom gutters** — tags `flux:table`; settings `bleed`.
- **Pagination** — tags `flux:table`.
- **Scroll to top** — tags `flux:table`; settings `pagination:scroll-to`.
- **Sortable** — tags `flux:table`, `flux:table.columns`, `flux:table.column`; settings `sortable`, `sorted`, `direction="desc"`.
- **Sticky header** — tags `flux:table`, `flux:table.columns`; settings `container:class="max-h-80"`, `sticky`.
- **Sticky columns** — tags `flux:table`, `flux:table.columns`, `flux:table.column`, `flux:table.rows`, `flux:table.row`; settings `container:class="max-h-80"`, `sticky`.

**Full page:** `references/source/components/table.md` (bundled) or [live](https://fluxui.dev/components/table.md). Read it for exact props, slots, and values.
