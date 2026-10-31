# Tabs

- **Availability:** Flux Pro.
- **Use:** Switch between related panels without leaving the page.
- **Main tags:** `flux:tab.group`, `flux:tabs`, `flux:tab`, `flux:tab.panel`.
- **Common props:** `findable`.

**Starter:**

```blade
<flux:tab.group><flux:tabs><flux:tab name="profile">Profile</flux:tab></flux:tabs><flux:tab.panel name="profile">Content</flux:tab.panel></flux:tab.group>
```

**Implementation:** Compose `flux:tab.group`, tabs, and matching panels. Names must match; consider findable or scrollable tabs for larger sets.

**Current source:** [Flux UI](https://fluxui.dev/components/tabs.md).
