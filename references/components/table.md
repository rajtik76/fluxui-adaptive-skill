# Table

- **Availability:** Flux (free).
- **Use:** Display rows and columns of structured data.
- **Main tags:** `flux:table`, `flux:table.columns`, `flux:table.column`, `flux:table.rows`, `flux:table.row`, `flux:table.cell`.
- **Common props:** `bleed`, `paginate`, `pagination:scroll-to`, `container:class`.

**Starter:**

```blade
<flux:table><flux:table.columns><flux:table.column>Name</flux:table.column></flux:table.columns><flux:table.rows><flux:table.row><flux:table.cell>Ada</flux:table.cell></flux:table.row></flux:table.rows></flux:table>
```

**Implementation:** Compose columns, rows, and cells. Sorting state, sticky sections, and Laravel pagination can be added where needed.

**Current source:** [Flux UI](https://fluxui.dev/components/table.md).
