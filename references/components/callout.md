# Callout

- **Availability:** Flux (free).
- **Use:** Draw attention to guidance, updates, or warnings.
- **Main tags:** `flux:callout`, `flux:callout.heading`, `flux:callout.text`, `flux:callout.link`.
- **Common props:** `icon`, `icon:variant`, `variant`, `color`, `inline`, `heading`, `text`, `actions`, `controls`.

**Starter:**

```blade
<flux:callout icon="information-circle"><flux:callout.heading>Notice</flux:callout.heading><flux:callout.text>Details</flux:callout.text></flux:callout>
```

**Implementation:** Compose heading and text inside the callout. Variants, colors, links, actions, and dismiss controls can match the message priority.

**Current source:** [Flux UI](https://fluxui.dev/components/callout.md).
