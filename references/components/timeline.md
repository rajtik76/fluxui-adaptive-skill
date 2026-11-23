# Timeline

- **Availability:** Flux Pro.
- **Use:** Present events or steps in sequence.
- **Main tags:** `flux:timeline`, `flux:timeline.item`, `flux:timeline.indicator`, `flux:timeline.content`, `flux:timeline.block`, `flux:timeline.subgrid`.

**Starter:**

```blade
<flux:timeline><flux:timeline.item><flux:timeline.indicator /><flux:timeline.content>Event</flux:timeline.content></flux:timeline.item></flux:timeline>
```

## How to customize

- Render items with an indicator and content to show events or process steps.
- Horizontal layout, status, indicator color, and size adapt the sequence.
- Block content, alignment, and spacing options help with denser timelines.

## Capabilities

- **Large** — tags `flux:timeline`, `flux:timeline.item`, `flux:timeline.indicator`, `flux:timeline.content`, `flux:heading`; settings `size="lg"`.
- **Horizontal** — tags `flux:timeline`, `flux:timeline.item`, `flux:timeline.indicator`, `flux:icon.credit-card`, `flux:timeline.content`; settings `horizontal`, `variant="micro"`.
- **Status** — tags `flux:timeline`, `flux:timeline.item`, `flux:timeline.indicator`, `flux:icon.credit-card`, `flux:timeline.content`; settings `horizontal`, `status="complete"`, `variant="micro"`, `status="current"`, `status="incomplete"`.
- **Indicator color** — tags `flux:timeline.indicator`, `flux:icon.x-mark`, `flux:icon.exclamation-triangle`, `flux:icon.check`; settings `color="red"`, `variant="micro"`, `color="amber"`, `color="green"`.
- **Bare indicator** — tags `flux:timeline`, `flux:timeline.item`, `flux:timeline.indicator`, `flux:icon.document-text`, `flux:timeline.content`; settings `variant="bare"`.
- **Block item** — tags `flux:timeline`, `flux:timeline.item`, `flux:timeline.block`, `flux:callout`, `flux:callout.heading`; settings `variant="secondary"`, `variant="ghost"`.
- **Block subgrid** — tags `flux:timeline`, `flux:timeline.item`, `flux:timeline.block`, `flux:timeline.subgrid`, `flux:avatar`; settings `size="xs"`, `variant="micro"`, `variant="input"`.
- **Alignment** — tags `flux:timeline`; settings `align="start|baseline|center|end"`.
- **Baseline adjustment** — tags `flux:timeline.item`, `flux:timeline.indicator`, `flux:timeline.content`, `flux:heading`; settings `align="baseline"`, `size="xl"`.
- **Spacing** — tags `flux:timeline`.

**Full page:** `references/source/components/timeline.md` (bundled) or [live](https://fluxui.dev/components/timeline.md). Read it for exact props, slots, and values.
