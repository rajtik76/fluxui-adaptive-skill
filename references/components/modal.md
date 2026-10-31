# Modal

- **Availability:** Flux (free).
- **Use:** Present a focused dialog or flyout over the page.
- **Main tags:** `flux:modal`, `flux:modal.trigger`, `flux:modal.close`.
- **Common props:** `name`, `flyout`, `variant`, `position`, `scroll`, `dismissible`, `escapable`, `closable`, `wire:model`, `close`, `cancel`.

**Starter:**

```blade
<flux:modal.trigger name="edit"><flux:button>Edit</flux:button></flux:modal.trigger><flux:modal name="edit">Content</flux:modal>
```

## How to customize

- Give each dialog a unique name and connect an opener through a trigger, Livewire, or JavaScript.
- Flyout and confirmation variants alter the interaction; scrolling options handle long content.
- Choose whether outside clicks and Escape dismiss it, and handle close/cancel events when state must be updated.

## Capabilities

- **Unique modal names** — tags `flux:modal`.
- **Livewire methods** — tags `flux:modal`.
- **JavaScript methods** — Use Flux modal controls from Alpine or the global `window.Flux` object.
- **Data binding** — tags `flux:modal`.
- **Close events** — tags `flux:modal`.
- **Cancel events** — tags `flux:modal`.
- **Disable click outside** — tags `flux:modal`.
- **Disable escape** — tags `flux:modal`.
- **Scrolling long content** — tags `flux:modal`; settings `scroll="body"`.
- **Confirmation** — tags `flux:modal.trigger`, `flux:button`, `flux:modal`, `flux:heading`, `flux:text`; settings `variant="danger"`, `variant="ghost"`.
- **Flyout** — tags `flux:modal.trigger`, `flux:button`, `flux:modal`, `flux:heading`, `flux:text`; settings `flyout`, `variant="primary"`.
- **Flyout positioning** — tags `flux:modal`; settings `flyout`, `position="left"`.
- **Floating flyout** — tags `flux:modal.trigger`, `flux:button`, `flux:modal`, `flux:heading`, `flux:subheading`; settings `flyout`, `variant="floating"`, `variant="filled"`, `variant="primary"`.

## Component API

- **`flux:modal`** — props: `name`, `flyout`, `variant` (values `default`, `floating`, `bare`, `flyout`), `position` (values `right`, `left`, `bottom`), `scroll` (values `body`), `dismissible` (default `true`), `escapable` (default `true`), `closable` (default `true`), `wire:model`; events: `close`, `cancel`; classs: `w-*`.
- **`flux:modal.trigger`** — props: `name`, `shortcut`.

**Implementation:** Give the modal a unique `name` and pair it with `flux:modal.trigger`; it can also be controlled through Livewire or JavaScript.

**Current source:** [Flux UI](https://fluxui.dev/components/modal.md).
