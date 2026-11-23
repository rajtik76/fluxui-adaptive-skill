# Phone

- **Availability:** Flux Pro.
- **Use:** Collect an international telephone number.
- **Main tags:** `flux:phone`.

**Starter:**

```blade
<flux:phone wire:model="phone" country="US" label="Phone" />
```

## How to customize

- Bind the telephone value and select an initial country where the form has that context.
- Limit or order the country list and adjust size or filled presentation.
- Flux formats and normalizes possible values, but server-side validation remains necessary.

## Capabilities

- **Basic usage** — tags `flux:phone`; settings `country="US"`.
- **Default country** — tags `flux:phone`; settings `country="GB"`.
- **Country list** — tags `flux:phone`.
- **Country order** — tags `flux:phone`.
- **Filled** — tags `flux:phone`; settings `variant="filled"`.
- **Sizes** — tags `flux:phone`; settings `size="sm"`, `size="xs"`.
- **Disabled and readonly** — tags `flux:phone`; settings `disabled`, `readonly`.
- **Invalid** — tags `flux:phone`; settings `invalid`.

**Full page:** `references/source/components/phone.md` (bundled) or [live](https://fluxui.dev/components/phone.md). Read it for exact props, slots, and values.
