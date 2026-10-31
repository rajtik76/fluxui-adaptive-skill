# Toast

- **Availability:** Flux (free).
- **Use:** Give short-lived feedback after an action.
- **Main tags:** `flux:toast`, `flux:toast.group`.
- **Common props:** `position`, `invert`.

**Starter:**

```blade
<flux:toast />
```

**Implementation:** Mount `flux:toast` in the layout and trigger messages via `Flux::toast()` or the supported JavaScript API. Variants, position, and duration are configurable.

**Current source:** [Flux UI](https://fluxui.dev/components/toast.md).
