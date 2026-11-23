# Textarea

- **Availability:** Flux (free).
- **Use:** Collect longer free-form text.
- **Main tags:** `flux:textarea`.

**Starter:**

```blade
<flux:textarea wire:model="notes" label="Notes" />
```

## How to customize

- Bind longer free-form text and provide a label or helpful placeholder.
- Set fixed rows for predictable height or enable auto-sizing for growing content.
- Resize settings control whether users can manually change the field size.

## Capabilities

- **With placeholder** — tags `flux:textarea`.
- **Fixed row height** — tags `flux:textarea`; settings `rows="2"`.
- **Auto-sizing textarea** — tags `flux:textarea`; settings `rows="auto"`.
- **Configure resize** — tags `flux:textarea`; settings `resize="vertical"`, `resize="none"`, `resize="horizontal"`, `resize="both"`.

**Full page:** `references/source/components/textarea.md` (bundled) or [live](https://fluxui.dev/components/textarea.md). Read it for exact props, slots, and values.
