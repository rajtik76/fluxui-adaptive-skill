# Profile

- **Availability:** Flux (free).
- **Use:** Show a compact avatar with an optional name and affordance.
- **Main tags:** `flux:profile`.
- **Common props:** `name`, `avatar`, `avatar:name`, `avatar:color`, `circle`, `initials`, `chevron`, `icon:trailing`, `icon:variant`.

**Starter:**

```blade
<flux:profile name="Ada Lovelace" />
```

## How to customize

- Show an avatar alone or with a name as a compact account identity.
- Circle shape, initials, trailing icon, and chevron options fit different layouts.
- Use it as a dropdown trigger when account actions follow the identity.

## Capabilities

- **With name** — tags `flux:profile`; settings `avatar`.
- **Without chevron** — tags `flux:profile`; settings `avatar`.
- **Circle avatar** — tags `flux:profile`; settings `circle`, `avatar`.
- **Avatar with initials** — tags `flux:profile`; settings `avatar:color="cyan"`, `initials="CP"`, `avatar:name="Caleb Porzio"`.
- **Custom trailing icon** — tags `flux:profile`; settings `icon:trailing`, `avatar`.
- **Profile menu** — tags `flux:dropdown`, `flux:profile`, `flux:navmenu`, `flux:text`, `flux:heading`; settings `avatar`.
- **Profile switcher** — tags `flux:dropdown`, `flux:profile`, `flux:menu`, `flux:menu.radio.group`, `flux:menu.radio`; settings `avatar`.

## Component API

- **`flux:profile`** — props: `name`, `avatar`, `avatar:name`, `avatar:color`, `circle`, `initials`, `chevron`, `icon:trailing`, `icon:variant` (values `micro`, `outline`); slots: `avatar`.

**Implementation:** Set avatar or initials and optional name. It can act as the trigger for a profile dropdown.

**Current source:** [Flux UI](https://fluxui.dev/components/profile.md).
