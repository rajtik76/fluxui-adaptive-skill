# Composer

- **Availability:** Flux Pro.
- **Use:** Collect a message with optional actions and rich text.
- **Main tags:** `flux:composer`.

**Starter:**

```blade
<flux:composer wire:model="message" label="Message" />
```

## How to customize

- Bind the message value and place the composer in a submit form.
- Use the actions slot or header to add controls; inline, input, rich-text, and height options change the editing surface.
- Choose when submission occurs and show disabled or invalid states consistently with form validation.

## Capabilities

- **With header** — tags `flux:composer`, `flux:icon`; settings `label:sr-only`.
- **Inline** — tags `flux:composer`, `flux:button`; settings `rows="1"`, `inline`, `label:sr-only`.
- **Input variant** — tags `flux:composer`.
- **Height** — tags `flux:composer`; settings `rows="4"`, `max-rows="8"`.
- **Submit behavior** — tags `flux:composer`; settings `submit="enter"`.
- **Rich text** — tags `flux:composer`, `flux:editor`, `flux:button`; settings `rows="3"`, `label:sr-only`.
- **Disabled** — tags `flux:composer`; settings `disabled`.
- **Invalid** — tags `flux:composer`; settings `label:sr-only`.

**Full page:** `references/source/components/composer.md` (bundled) or [live](https://fluxui.dev/components/composer.md). Read it for exact props, slots, and values.
