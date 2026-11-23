# Callout

- **Availability:** Flux (free).
- **Use:** Draw attention to guidance, updates, or warnings.
- **Main tags:** `flux:callout`, `flux:callout.heading`, `flux:callout.text`, `flux:callout.link`.

**Starter:**

```blade
<flux:callout icon="information-circle"><flux:callout.heading>Notice</flux:callout.heading><flux:callout.text>Details</flux:callout.text></flux:callout>
```

## How to customize

- Compose heading and supporting text, then choose icon, variant, and color for the message.
- Add links or actions when the user has a next step; inline layout is available for tighter placements.
- Use a dismiss control only when hiding the notice makes sense for the application.

## Capabilities

- **Icon inside heading** — tags `flux:callout`, `flux:callout.heading`, `flux:callout.text`; settings `icon`.
- **With actions** — tags `flux:callout`, `flux:callout.heading`, `flux:callout.text`, `flux:button`; settings `icon`, `variant="ghost"`.
- **Inline actions** — tags `flux:callout`, `flux:callout.heading`, `flux:button`, `flux:callout.text`; settings `icon`, `variant="secondary"`, `inline`, `variant="ghost"`.
- **Dismissible** — tags `flux:callout`, `flux:callout.heading`, `flux:text`, `flux:button`, `flux:callout.text`; settings `icon`, `variant="secondary"`, `inline`, `variant="ghost"`.
- **Variants** — tags `flux:callout`; settings `variant="secondary"`, `icon`, `heading`, `variant="success"`, `variant="warning"`, `variant="danger"`.
- **Colors** — tags `flux:callout`; settings `color="zinc"`, `color="red"`, `color="orange"`, `color="amber"`, `color="yellow"`, `color="lime"`.
- **Custom icon** — tags `flux:callout`, `flux:callout.heading`, `flux:callout.text`.
- **Feature spotlight** — tags `flux:callout`, `flux:callout.heading`, `flux:callout.text`, `flux:callout.link`; settings `icon`, `color="purple"`.
- **Premium upsell** — tags `flux:callout`, `flux:callout.heading`, `flux:callout.text`, `flux:button`; settings `icon`, `color="blue"`, `inline`.
- **Upgrade offer** — tags `flux:callout`, `flux:callout.heading`, `flux:button`; settings `icon`, `color="lime"`, `inline`.
- **Engagement prompt** — tags `flux:callout`, `flux:callout.heading`, `flux:badge`, `flux:callout.text`, `flux:button`; settings `variant="secondary"`, `icon`, `color="purple"`, `variant="ghost"`.

**Full page:** `references/source/components/callout.md` (bundled) or [live](https://fluxui.dev/components/callout.md). Read it for exact props, slots, and values.
