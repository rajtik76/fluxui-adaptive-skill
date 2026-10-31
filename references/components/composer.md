# Composer

- **Availability:** Flux Pro.
- **Use:** Collect a message with optional actions and rich text.
- **Main tags:** `flux:composer`.
- **Common props:** `wire:model`, `name`, `placeholder`, `label`, `label:sr-only`, `description`, `description:sr-only`, `rows`, `max-rows`, `inline`, `submit`, `disabled`.

**Starter:**

```blade
<flux:composer wire:model="message" label="Message" />
```

**Implementation:** Bind its content with Livewire inside a form. Choose submit behavior, inline layout, input mode, and action slots to fit the workflow.

**Current source:** [Flux UI](https://fluxui.dev/components/composer.md).
