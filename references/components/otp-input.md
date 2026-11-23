# OTP Input

- **Availability:** Flux (free).
- **Use:** Enter a fixed-length verification code.
- **Main tags:** `flux:otp`, `flux:otp.input`, `flux:otp.separator`, `flux:otp.group`.

**Starter:**

```blade
<flux:otp wire:model="code" length="6" />
```

## How to customize

- Set the expected code length and bind the result to Livewire.
- Choose numeric or alphanumeric input, private display, or auto-submit based on the verification flow.
- Groups and separators can visually divide longer codes without changing their stored value.

## Capabilities

- **Example usage** — tags `flux:card`, `flux:heading`, `flux:text`, `flux:otp`, `flux:button`; settings `length="6"`.
- **Autosubmit** — tags `flux:heading`, `flux:text`, `flux:otp`; settings `length="6"`, `submit="auto"`.
- **Alphanumeric** — tags `flux:otp`; settings `length="10"`, `mode="alphanumeric"`.
- **Private** — tags `flux:otp`; settings `length="4"`, `private`.
- **Separator** — tags `flux:otp`, `flux:otp.input`, `flux:otp.separator`.
- **Group** — tags `flux:otp`, `flux:otp.group`, `flux:otp.input`.
- **Group separator** — tags `flux:otp`, `flux:otp.group`, `flux:otp.input`, `flux:otp.separator`.

**Full page:** `references/source/components/otp-input.md` (bundled) or [live](https://fluxui.dev/components/otp-input.md). Read it for exact props, slots, and values.
