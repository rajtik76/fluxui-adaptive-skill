# Button

- **Availability:** Flux (free).
- **Use:** Trigger an action or present a link.
- **Main tags:** `flux:button`, `flux:button.group`.
- **Common props:** `as`, `href`, `type`, `variant`, `color`, `size`, `icon`, `icon:variant`, `icon:trailing`, `square`, `align`, `inset`.

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

## Component API

- **`flux:button`** — props: `as` (values `button`, `a`, `div`), `href`, `type` (values `button`, `submit`), `variant` (values `outline`, `primary`, `filled`, `danger`, `ghost`, `subtle`; default `outline`), `color`, `size` (values `base`, `sm`, `xs`), `icon`, `icon:variant` (values `outline`, `solid`, `mini`, `micro`; default `micro`), `icon:trailing`, `square`, `align` (values `start`, `center`, `end`; default `center`), `inset` (values `top`, `bottom`, `left`, `right`), `loading` (default `true`), `tooltip`, `tooltip:position` (values `top`, `bottom`, `left`, `right`; default `top`), `tooltip:kbd`, `kbd`; CSS: `class`.

**Implementation:** Choose `type="submit"` for form submission or `href` for navigation. `variant`, `color`, `size`, and icon props change appearance; loading is available for Livewire actions.

**Current source:** [Flux UI](https://fluxui.dev/components/button.md).
