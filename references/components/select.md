# Select

- **Availability:** Flux (free) for the native select; the listbox, searchable, multiple, combobox, backend-search, and option-creation variants require Flux Pro.
- **Use:** Choose from a controlled set of options.
- **Main tags:** `flux:select`, `flux:select.option`, `flux:select.group`, `flux:select.option.create`, `flux:select.option.empty`, `flux:select.button`.
- **Common props:** `wire:model`, `placeholder`, `label`, `description`, `description:trailing`, `badge`, `size`, `variant`, `multiple`, `filter`, `searchable`, `empty`.

**Starter:**

```blade
<flux:select wire:model="role" label="Role"><flux:select.option value="admin">Admin</flux:select.option></flux:select>
```

## How to customize

- Start with a native option list when simple choice is enough; use listbox or combobox for richer interaction.
- Listbox can add search, multiple selection, icons, descriptions, and clear controls. Combobox supports typed and server-backed search.
- Keep option values stable; for backend creation or filtering, use the documented loading, empty, and validation states.

## Capabilities

- **Small** — tags `flux:select`, `flux:select.option`; settings `size="sm"`.
- **Option groups** — tags `flux:select`, `flux:select.group`, `flux:select.option`.
- **Custom select (Pro)** — tags `flux:select`, `flux:select.option`; settings `variant="listbox"`.
- **The `button` slot (Pro)** — tags `flux:select`, `flux:select.button`, `flux:select.option`; settings `variant="listbox"`.
- **Clearable (Pro)** — tags `flux:select`; settings `variant="listbox"`, `clearable`.
- **With a prefix (Pro)** — tags `flux:select`, `flux:select.option`; settings `variant="listbox"`, `prefix="Compare to"`.
- **With icons (Pro)** — tags `flux:select`, `flux:select.option`; settings `variant="listbox"`, `icon`.
- **With descriptions (Pro)** — tags `flux:select`, `flux:select.option`; settings `variant="listbox"`.
- **With avatars (Pro)** — tags `flux:select`, `flux:select.option`; settings `variant="listbox"`, `avatar`.
- **With custom content (Pro)** — tags `flux:select`, `flux:select.option`; settings `variant="listbox"`.
- **Customizing the dropdown width (Pro)** — tags `flux:select`, `flux:select.option`; settings `variant="listbox"`, `options:class="min-w-72"`, `icon`.
- **Searchable select (Pro)** — tags `flux:select`, `flux:select.option`; settings `variant="listbox"`, `searchable`.
- **The `search` slot (Pro)** — tags `flux:select`, `flux:select.search`; settings `variant="listbox"`, `searchable`.
- **Search keywords (Pro)** — tags `flux:select`, `flux:select.option`; settings `variant="listbox"`, `searchable`, `keywords`.
- **Multiple select (Pro)** — tags `flux:select`, `flux:select.option`; settings `variant="listbox"`, `multiple`.
- **Selected suffix (Pro)** — tags `flux:select`; settings `variant="listbox"`, `selected-suffix="industries selected"`, `multiple`.
- **Checkbox indicator (Pro)** — tags `flux:select`; settings `variant="listbox"`, `multiple`.
- **Clearing search (Pro)** — tags `flux:select`; settings `variant="listbox"`, `searchable`, `multiple`, `clear="close"`.
- **Combobox (Pro)** — tags `flux:select`, `flux:select.option`; settings `variant="combobox"`.
- **The `input` slot (Pro)** — tags `flux:select`, `flux:select.input`; settings `variant="combobox"`.
- **Backend search (Pro)** — tags `flux:select`, `flux:select.input`, `flux:select.option`; settings `variant="combobox"`.
- **Create option (Pro)** — tags `flux:select`, `flux:select.input`, `flux:select.option`, `flux:select.option.create`; settings `variant="combobox"`, `min-length="2"`.
- **With backend search (Pro)** — tags `flux:select`, `flux:select.input`, `flux:select.option`, `flux:select.option.create`; settings `variant="combobox"`, `min-length="2"`.
- **With listbox variant (Pro)** — After creating a value during backend search, clear the search input to avoid a redundant request.
- **Loading message (Pro)** — tags `flux:select`, `flux:select.option.empty`; settings `variant="combobox"`, `when-loading="Loading projects..."`.
- **With validation (Pro)** — tags `flux:select`, `flux:select.input`, `flux:select.option.create`; settings `variant="combobox"`, `min-length="2"`.
- **With modal (Pro)** — tags `flux:select`, `flux:select.option`, `flux:select.option.create`, `flux:modal`, `flux:heading`; settings `variant="listbox"`, `modal="create-project"`, `size="lg"`, `variant="primary"`.

## Component API

- **`flux:select`** — props: `wire:model`, `placeholder`, `label`, `description`, `description:trailing`, `badge`, `size` (values `sm`, `xs`), `variant` (values `default`, `listbox`, `combobox`), `multiple`, `filter`, `searchable`, `empty` (default `No results found`), `clearable`, `prefix`, `selected-suffix`, `clear` (values `select`, `close`), `position` (values `top`, `right`, `bottom`, `left`), `align` (values `start`, `center`, `end`; default `start`), `options:class`, `disabled`, `invalid`; slots: `trigger`, `empty`.
- **`flux:select.option`** — props: `value`, `label`, `selected-label`, `keywords`, `icon`, `icon:variant` (values `outline`, `solid`, `mini`, `micro`; default `mini`), `icon:class`, `avatar`, `avatar:*`, `description`, `disabled`.
- **`flux:select.group`** — props: `label`.
- **`flux:select.option.create`** — props: `min-length`, `modal`, `wire:click`.
- **`flux:select.option.empty`** — props: `when-loading`.
- **`flux:select.button`** — props: `placeholder`, `invalid`, `size` (values `sm`, `xs`), `disabled`, `clearable`.
- **`flux:select.input`** — props: `placeholder`, `invalid`, `size` (values `sm`, `xs`).
- **`flux:select.search`** — props: `placeholder`, `icon`, `clearable` (default `true`).

**Implementation:** Bind the select and add `flux:select.option` values. Native and custom variants differ; search, grouping, and multiple selection depend on the chosen variant.

**Current source:** [Flux UI](https://fluxui.dev/components/select.md).
