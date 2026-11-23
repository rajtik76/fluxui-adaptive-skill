# Tabs

- **Availability:** Flux Pro.
- **Use:** Switch between related panels without leaving the page.
- **Main tags:** `flux:tab.group`, `flux:tabs`, `flux:tab`, `flux:tab.panel`.

**Starter:**

```blade
<flux:tab.group><flux:tabs><flux:tab name="profile">Profile</flux:tab></flux:tabs><flux:tab.panel name="profile">Content</flux:tab.panel></flux:tab.group>
```

## How to customize

- Give tabs and panels matching names so selection reveals the corresponding content.
- Icons, segmented or pill styles, and scrollable strips adapt to different density.
- Findable and dynamic tabs support larger or changing sets of panels.

## Capabilities

- **Findable tabs** — tags `flux:tab.group`, `flux:tabs`, `flux:tab`, `flux:tab.panel`; settings `findable`, `selected`.
- **With icons** — tags `flux:tab.group`, `flux:tabs`, `flux:tab`, `flux:tab.panel`; settings `icon`.
- **Padded edges** — tags `flux:tabs`, `flux:tab`.
- **Scrollable tabs** — tags `flux:tab.group`, `flux:tabs`, `flux:tab`, `flux:tab.panel`; settings `scrollable`.
- **Faded edge** — tags `flux:tab.group`, `flux:tabs`, `flux:tab`, `flux:tab.panel`; settings `scrollable`, `scrollable:fade`.
- **Segmented tabs** — tags `flux:tabs`, `flux:tab`; settings `variant="segmented"`.
- **Segmented with icons** — tags `flux:tabs`, `flux:tab`; settings `variant="segmented"`, `icon`.
- **Small segmented tabs** — tags `flux:tabs`, `flux:tab`; settings `variant="segmented"`, `size="sm"`.
- **Pill tabs** — tags `flux:tabs`, `flux:tab`; settings `variant="pills"`.
- **Dynamic tabs** — tags `flux:tab.group`, `flux:tabs`, `flux:tab`, `flux:tab.panel`; settings `icon`, `action`.

**Full page:** `references/source/components/tabs.md` (bundled) or [live](https://fluxui.dev/components/tabs.md). Read it for exact props, slots, and values.
