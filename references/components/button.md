# Button

- **Availability:** Flux (free).
- **Use:** Trigger an action or present a link.
- **Main tags:** `flux:button`, `flux:button.group`.

**Starter:**

```blade
<flux:button type="submit" variant="primary">Save</flux:button>
```

## How to customize

- Choose a variant, color, and size based on the action hierarchy; make form submission explicit with button type.
- Icons can lead or trail the label, and square buttons suit icon-only controls. Loading feedback integrates with Livewire actions.
- Group or attach related buttons; a button can also render as a link or input when that semantic element is needed.

## Capabilities

- **Variants** — tags `flux:button`; settings `variant="primary"`, `variant="filled"`, `variant="danger"`, `variant="ghost"`, `variant="subtle"`.
- **Colors** — tags `flux:button`; settings `variant="primary"`, `color="blue"`, `variant="filled"`, `variant="outline"`, `variant="ghost"`, `variant="subtle"`.
- **Outline colors** — tags `flux:button`; settings `variant="outline"`, `color="blue"`, `color="green"`, `color="red"`.
- **Sizes** — tags `flux:button`; settings `size="sm"`, `size="xs"`.
- **Icons** — tags `flux:button`; settings `icon`, `icon:trailing`, `variant="subtle"`.
- **Loading** — tags `flux:button`.
- **Full width** — tags `flux:button`; settings `variant="primary"`.
- **Button groups** — tags `flux:button.group`, `flux:button`.
- **Icon group** — tags `flux:button.group`, `flux:button`; settings `icon`.
- **Attached button** — tags `flux:button.group`, `flux:button`; settings `icon`.
- **As a link** — tags `flux:button`; settings `icon:trailing`.
- **As an input** — tags `flux:input`; settings `as="button"`, `icon`, `kbd`.
- **Square** — tags `flux:button`; settings `square`.
- **Inset** — tags `flux:heading`, `flux:button`; settings `size="sm"`, `icon`, `variant="ghost"`, `inset`.

**Full page:** `references/source/components/button.md` (bundled) or [live](https://fluxui.dev/components/button.md). Read it for exact props, slots, and values.
