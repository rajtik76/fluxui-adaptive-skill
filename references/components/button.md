# Button

- **Availability:** Flux (free).
- **Use:** Trigger an action or present a link.
- **Main tags:** `flux:button`, `flux:button.group`.
- **Common props:** `as`, `href`, `type`, `variant`, `color`, `size`, `icon`, `icon:variant`, `icon:trailing`, `square`, `align`, `inset`.

**Starter:**

```blade
<flux:button type="submit" variant="primary">Save</flux:button>
```

**Implementation:** Choose `type="submit"` for form submission or `href` for navigation. `variant`, `color`, `size`, and icon props change appearance; loading is available for Livewire actions.

**Current source:** [Flux UI](https://fluxui.dev/components/button.md).
