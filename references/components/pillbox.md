# Pillbox

- **Availability:** Flux Pro.
- **Use:** Choose several values shown as removable pills.
- **Main tags:** `flux:pillbox`, `flux:pillbox.option`, `flux:pillbox.option.create`, `flux:pillbox.option.empty`, `flux:pillbox.search`, `flux:pillbox.trigger`.

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

**Full page:** `references/source/components/pillbox.md` (bundled) or [live](https://fluxui.dev/components/pillbox.md). Read it for exact props, slots, and values.
