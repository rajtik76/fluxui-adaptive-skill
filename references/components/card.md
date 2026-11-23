# Card

- **Availability:** Flux (free).
- **Use:** Group related content with a consistent container.
- **Main tags:** `flux:card`, `flux:card.header`, `flux:card.heading`, `flux:card.subheading`, `flux:card.actions`, `flux:card.body`.

**Starter:**

```blade
<flux:card><flux:card.header><flux:card.heading>Profile</flux:card.heading></flux:card.header>Content</flux:card>
```

## How to customize

- Use the card as a layout container with optional header, body, footer, and actions rather than manually recreating spacing.
- Variant, size, divider, and body treatment determine how strongly those regions are separated.
- Bleed or inset content when a table, media, or controls should align with the card edge.

## Capabilities

- **Simple card** — tags `flux:card`, `flux:heading`, `flux:text`, `flux:button`; settings `size="lg"`, `variant="danger"`.
- **Variants** — tags `flux:card`, `flux:heading`, `flux:text`; settings `variant="muted"`, `variant="soft"`, `variant="outline"`, `variant="filled"`.
- **Sizes** — tags `flux:card`, `flux:card.header`, `flux:card.heading`, `flux:card.actions`, `flux:button`; settings `size="xs"`, `body="separated"`, `size="sm"`, `size="md"`, `size="lg"`.
- **Body treatments** — Use header, body, and footer regions; the `body` prop adjusts their separation.
- **Seamless** — tags `flux:card`, `flux:card.header`, `flux:card.heading`, `flux:card.subheading`, `flux:card.body`; settings `body="seamless"`.
- **Inset** — tags `flux:card`; settings `body="inset"`, `variant="soft"`.
- **Flush** — tags `flux:card`; settings `body="flush"`, `variant="soft"`.
- **Divided** — tags `flux:card`; settings `body="divided"`, `divider="inset"`.
- **Separated** — tags `flux:card`; settings `body="separated"`.
- **Bleed** — Extend selected content to the card edge instead of leaving it inside padding.
- **Images** — tags `flux:card`, `flux:card.body`, `flux:card.bleed`, `flux:card.footer`, `flux:card.heading`; settings `body="inset"`, `size="sm"`, `variant="ghost"`.
- **Tables** — tags `flux:card`, `flux:card.header`, `flux:card.heading`, `flux:card.actions`, `flux:button`; settings `variant="muted"`, `body="flush"`, `size="sm"`, `variant="filled"`.
- **Outside a card** — tags `flux:card.header`, `flux:card.heading`, `flux:card.actions`, `flux:button`, `flux:card`; settings `size="lg"`, `size="sm"`, `variant="outline"`, `variant="subtle"`.
- **Inside a body** — tags `flux:card`, `flux:card.header`, `flux:card.heading`, `flux:card.subheading`, `flux:card.body`; settings `body="inset"`, `variant="soft"`, `size="sm"`, `variant="strong"`, `variant="subtle"`, `variant="ghost"`.
- **Link card** — tags `flux:card`, `flux:heading`, `flux:icon`, `flux:text`; settings `size="xs"`, `variant="micro"`.

**Full page:** `references/source/components/card.md` (bundled) or [live](https://fluxui.dev/components/card.md). Read it for exact props, slots, and values.
