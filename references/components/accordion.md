# Accordion

- **Availability:** Flux Pro.
- **Use:** Show expandable sections such as FAQs.
- **Main tags:** `flux:accordion`, `flux:accordion.item`, `flux:accordion.heading`, `flux:accordion.content`.
- **Common props:** `variant`, `transition`, `exclusive`.

**Starter:**

```blade
<flux:accordion><flux:accordion.item heading="Question">Answer</flux:accordion.item></flux:accordion>
```

**Implementation:** Place item, heading, and content tags inside the accordion. Use `exclusive` for one open item at a time; items can start `expanded` or be `disabled`.

**Current source:** [Flux UI](https://fluxui.dev/components/accordion.md).
