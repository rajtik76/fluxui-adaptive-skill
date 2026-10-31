# Pillbox

- **Availability:** Flux Pro.
- **Use:** Choose several values shown as removable pills.
- **Main tags:** `flux:pillbox`, `flux:pillbox.option`, `flux:pillbox.option.create`, `flux:pillbox.option.empty`, `flux:pillbox.search`, `flux:pillbox.trigger`.
- **Common props:** `wire:model`, `placeholder`, `label`, `description`, `size`, `searchable`, `search:placeholder`, `filter`, `disabled`, `invalid`, `trigger`, `search`.

**Starter:**

```blade
<flux:pillbox wire:model="tags" multiple><flux:pillbox.option value="design">Design</flux:pillbox.option></flux:pillbox>
```

## How to customize

- Bind multiple selected values and provide options that appear as removable pills.
- Search, icons, combobox behavior, and option creation help with larger vocabularies.
- For server-backed suggestions, use the documented backend-search and loading states.

## Capabilities

- **Small** — tags `flux:pillbox`, `flux:pillbox.option`; settings `size="sm"`.
- **Searchable** — tags `flux:pillbox`, `flux:pillbox.option`; settings `searchable`.
- **Custom search placeholder** — tags `flux:pillbox`; settings `searchable`, `search:placeholder="Filter skills..."`.
- **With icons** — tags `flux:pillbox`, `flux:pillbox.option`, `flux:icon.code-bracket`, `flux:icon.server`, `flux:icon.cloud`.
- **Combobox** — tags `flux:pillbox`, `flux:pillbox.option`.
- **Create option** — tags `flux:pillbox`, `flux:pillbox.input`, `flux:pillbox.option`, `flux:pillbox.option.create`; settings `min-length="2"`.
- **With backend search** — tags `flux:pillbox`, `flux:pillbox.input`, `flux:pillbox.option`, `flux:pillbox.option.create`; settings `min-length="2"`.
- **Loading message** — tags `flux:pillbox`, `flux:pillbox.option.empty`; settings `when-loading="Loading tags..."`.
- **With validation** — tags `flux:pillbox`, `flux:pillbox.input`, `flux:pillbox.option.create`; settings `min-length="2"`.
- **With modal** — tags `flux:pillbox`, `flux:pillbox.option.create`, `flux:pillbox.option`, `flux:modal`, `flux:heading`; settings `modal="create-tag"`, `size="lg"`.

## Component API

- **`flux:pillbox`** — props: `wire:model`, `placeholder`, `label`, `description`, `size` (values `sm`), `searchable`, `search:placeholder`, `filter`, `disabled`, `invalid`; slots: `trigger`, `search`, `empty`.
- **`flux:pillbox.option`** — props: `value`, `label`, `selected-label`, `disabled`, `filterable`.
- **`flux:pillbox.option.create`** — props: `min-length`, `modal`, `wire:click`.
- **`flux:pillbox.option.empty`** — props: `when-loading`.
- **`flux:pillbox.search`** — props: `placeholder`, `icon`, `clearable` (default `true`).
- **`flux:pillbox.trigger`** — props: `placeholder`, `invalid`, `size` (values `sm`), `clearable`.

**Implementation:** Bind an array-like selection and add `flux:pillbox.option` choices. Search, creation, and backend search patterns are available.

**Current source:** [Flux UI](https://fluxui.dev/components/pillbox.md).
