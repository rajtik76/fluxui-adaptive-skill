# Table

- **Availability:** Flux (free).
- **Use:** Display rows and columns of structured data.
- **Main tags:** `flux:table`, `flux:table.columns`, `flux:table.column`, `flux:table.rows`, `flux:table.row`, `flux:table.cell`.
- **Common props:** `bleed`, `paginate`, `pagination:scroll-to`, `container:class`.

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

## Component API

- **`flux:table`** — props: `bleed`, `paginate`, `pagination:scroll-to` (default `body`), `container:class`.
- **`flux:table.columns`** — props: `sticky`.
- **`flux:table.column`** — props: `align` (values `start`, `center`, `end`), `sortable`, `sorted`, `direction` (values `asc`, `desc`), `sticky`.
- **`flux:table.row`** — props: `key`, `sticky`.
- **`flux:table.cell`** — props: `align` (values `start`, `center`, `end`), `variant` (values `default`, `strong`), `sticky`.

**Implementation:** Compose columns, rows, and cells. Sorting state, sticky sections, and Laravel pagination can be added where needed.

**Current source:** [Flux UI](https://fluxui.dev/components/table.md).
