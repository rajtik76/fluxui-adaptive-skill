# Tabs

- **Availability:** Flux Pro.
- **Use:** Switch between related panels without leaving the page.
- **Main tags:** `flux:tab.group`, `flux:tabs`, `flux:tab`, `flux:tab.panel`.
- **Common props:** `findable`.

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

## Component API

- **`flux:tab.group`** — props: `findable`.
- **`flux:tabs`** — props: `wire:model`, `variant` (values `default`, `segmented`, `pills`), `size` (values `base`, `sm`), `scrollable`, `scrollable:scrollbar` (values `hide`), `scrollable:fade`.
- **`flux:tab`** — props: `name`, `icon`, `icon:trailing`, `icon:variant` (values `outline`, `solid`, `mini`, `micro`), `selected`, `action`, `accent`, `size` (values `base`, `sm`), `disabled`.
- **`flux:tab.panel`** — props: `name`, `selected`.

**Implementation:** Compose `flux:tab.group`, tabs, and matching panels. Names must match; consider findable or scrollable tabs for larger sets.

**Current source:** [Flux UI](https://fluxui.dev/components/tabs.md).
