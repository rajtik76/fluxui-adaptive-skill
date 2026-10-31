# Pillbox

- **Availability:** Flux Pro.
- **Use:** Choose several values shown as removable pills.
- **Main tags:** `flux:pillbox`, `flux:pillbox.option`, `flux:pillbox.option.create`, `flux:pillbox.option.empty`, `flux:pillbox.search`, `flux:pillbox.trigger`.
- **Common props:** `wire:model`, `placeholder`, `label`, `description`, `size`, `searchable`, `search:placeholder`, `filter`, `disabled`, `invalid`, `trigger`, `search`.

**Starter:**

```blade
<flux:pillbox wire:model="tags" multiple><flux:pillbox.option value="design">Design</flux:pillbox.option></flux:pillbox>
```

**Implementation:** Bind an array-like selection and add `flux:pillbox.option` choices. Search, creation, and backend search patterns are available.

**Current source:** [Flux UI](https://fluxui.dev/components/pillbox.md).
