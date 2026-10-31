# Icon

- **Availability:** Flux (free).
- **Use:** Add a named icon from the configured icon set.
- **Main tags:** `flux:icon.*`.
- **Common props:** `variant`.

**Starter:**

```blade
<flux:icon.bolt />
```

## How to customize

- Use a verified icon name and choose outline, solid, mini, or micro appearance as appropriate.
- Size and color can follow surrounding text; a spinner variant covers loading states.
- Import Lucide icons or provide custom Blade icon views when Heroicons does not include the needed symbol.

## Capabilities

- **Variants** — tags `flux:icon.bolt`; settings `variant="solid"`, `variant="mini"`, `variant="micro"`.
- **Sizes** — tags `flux:icon.bolt`.
- **Color** — tags `flux:icon.bolt`; settings `variant="solid"`.
- **Loading spinner** — tags `flux:icon.loading`.
- **Dynamic icons** — tags `flux:icon`.
- **Lucide icons** — Import Lucide icons into the project through the Flux Artisan command before using them.
- **Custom icons** — Provide project Blade icon views under `resources/views/flux/icon`.

## Component API

- **`flux:icon.*`** — props: `variant` (values `outline`, `solid`, `mini`, `micro`); classs: `size-*`, `text-*`.

**Implementation:** Use a concrete `flux:icon.<name>` tag. Verify icon names; choose a variant and size supported by the installed set.

**Current source:** [Flux UI](https://fluxui.dev/components/icon.md).
