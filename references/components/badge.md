# Badge

- **Availability:** Flux (free).
- **Use:** Mark status or category with compact text.
- **Main tags:** `flux:badge`, `flux:badge.close`.

**Starter:**

```blade
<flux:badge color="green">Active</flux:badge>
```

## How to customize

- Choose color and visual variant to signal status without turning it into the primary action.
- Size, rounded shape, and optional leading or trailing icons adjust density and emphasis.
- A badge can act as a button or include a close control when the label is interactive.

## Capabilities

- **Sizes** — tags `flux:badge`; settings `size="sm"`, `size="lg"`.
- **Icons** — tags `flux:badge`; settings `icon`, `icon:trailing`.
- **Rounded** — tags `flux:badge`; settings `rounded`, `icon`.
- **As button** — tags `flux:badge`; settings `as="button"`, `rounded`, `icon`, `size="lg"`.
- **With close button** — tags `flux:badge`, `flux:badge.close`.
- **Colors** — tags `flux:badge`; settings `color="zinc"`, `color="red"`, `color="orange"`, `color="amber"`, `color="yellow"`, `color="lime"`.
- **Solid variant** — tags `flux:badge`; settings `variant="solid"`, `color="zinc"`, `color="red"`, `color="orange"`, `color="amber"`, `color="yellow"`.
- **Inset** — tags `flux:heading`, `flux:badge`, `flux:text`; settings `color="lime"`, `inset="top bottom"`.

**Full page:** `references/source/components/badge.md` (bundled) or [live](https://fluxui.dev/components/badge.md). Read it for exact props, slots, and values.
