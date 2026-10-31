# OTP Input

- **Availability:** Flux (free).
- **Use:** Enter a fixed-length verification code.
- **Main tags:** `flux:otp`, `flux:otp.input`, `flux:otp.separator`, `flux:otp.group`.
- **Common props:** `wire:model`, `value`, `length`, `mode`, `private`, `submit`, `autocomplete`.

**Starter:**

```blade
<flux:otp wire:model="code" length="6" />
```

**Implementation:** Bind `flux:otp` to Livewire and set `length`; alphanumeric, private, grouped, and submit modes are available.

**Current source:** [Flux UI](https://fluxui.dev/components/otp-input.md).
