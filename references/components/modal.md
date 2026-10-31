# Modal

- **Availability:** Flux (free).
- **Use:** Present a focused dialog or flyout over the page.
- **Main tags:** `flux:modal`, `flux:modal.trigger`, `flux:modal.close`.
- **Common props:** `name`, `flyout`, `variant`, `position`, `scroll`, `dismissible`, `escapable`, `closable`, `wire:model`, `close`, `cancel`.

**Starter:**

```blade
<flux:modal.trigger name="edit"><flux:button>Edit</flux:button></flux:modal.trigger><flux:modal name="edit">Content</flux:modal>
```

**Implementation:** Give the modal a unique `name` and pair it with `flux:modal.trigger`; it can also be controlled through Livewire or JavaScript.

**Current source:** [Flux UI](https://fluxui.dev/components/modal.md).
