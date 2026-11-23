# Popover

- **Availability:** Flux Pro.
- **Use:** Show custom floating content from a trigger.
- **Main tags:** `flux:dropdown`, `flux:popover`.

**Starter:**

```blade
<flux:dropdown><flux:button>Details</flux:button><flux:popover>More information</flux:popover></flux:dropdown>
```

## How to customize

- Use a dropdown wrapper for one trigger and a popover containing arbitrary content.
- Hover triggering is available for lightweight previews; click triggering suits interactive content.
- Tune placement, alignment, gap, and offset so the panel stays near its trigger.

## Capabilities

- **Hover trigger** — tags `flux:dropdown`, `flux:avatar`, `flux:heading`, `flux:popover`, `flux:text`; settings `hover`, `position="bottom"`, `align="start"`.
- **Position** — tags `flux:dropdown`, `flux:button`, `flux:popover`; settings `position="top"`, `align="start"`, `position="right"`, `align="center"`, `position="left"`, `position="bottom"`.
- **Gap & offset** — tags `flux:dropdown`, `flux:button`, `flux:popover`.
- **Category picker** — tags `flux:dropdown`, `flux:button`, `flux:badge`, `flux:popover`, `flux:checkbox.group`.
- **Feedback** — tags `flux:dropdown`, `flux:button`, `flux:popover`, `flux:radio.group`, `flux:radio`.
- **Event details** — tags `flux:dropdown`, `flux:heading`, `flux:text`, `flux:popover`, `flux:radio.group`; settings `position="bottom center"`.

**Full page:** `references/source/components/popover.md` (bundled) or [live](https://fluxui.dev/components/popover.md). Read it for exact props, slots, and values.
