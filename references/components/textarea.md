# Textarea

- **Availability:** Flux (free).
- **Use:** Collect longer free-form text.
- **Main tags:** `flux:textarea`.
- **Common props:** `wire:model`, `placeholder`, `label`, `description`, `description:trailing`, `badge`, `rows`, `resize`, `invalid`.

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

## Component API

- **`flux:textarea`** — props: `wire:model`, `placeholder`, `label`, `description`, `description:trailing`, `badge`, `rows` (default `4`), `resize` (values `vertical`, `horizontal`, `both`, `none`), `invalid`.

**Implementation:** Bind with Livewire; use rows, resize, or auto-sizing behavior to fit the expected length.

**Current source:** [Flux UI](https://fluxui.dev/components/textarea.md).
