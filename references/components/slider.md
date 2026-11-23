# Slider

- **Availability:** Flux Pro.
- **Use:** Adjust a numeric value by dragging along a track.
- **Main tags:** `flux:slider`, `flux:slider.tick`.

**Starter:**

```blade
<flux:slider wire:model="amount" min="0" max="100" />
```

## How to customize

- Bind a numeric value and set minimum, maximum, and step to the actual allowed range.
- An accompanying input, large steps, ticks, and labels improve precision.
- Range mode adds two thumbs; style the track and thumbs for the surrounding design.

## Capabilities

- **Min/max/step** — tags `flux:slider`; settings `min="0"`, `max="100"`, `step="10"`.
- **Displaying value** — tags `flux:field`, `flux:label`, `flux:slider`.
- **With input** — tags `flux:field`, `flux:label`, `flux:slider`, `flux:input`.
- **Big steps** — tags `flux:slider`; settings `step="1"`, `big-step="10"`.
- **Step marks** — tags `flux:slider`, `flux:slider.tick`; settings `min="1"`, `max="5"`.
- **Step dots** — tags `flux:slider`, `flux:slider.tick`; settings `tick:position="inside"`, `min="1"`, `max="5"`, `track:class="h-5"`, `thumb:class="size-6"`, `variant="dot"`.
- **Numbered steps** — tags `flux:slider`, `flux:slider.tick`; settings `min="1"`, `max="5"`.
- **Custom steps** — tags `flux:slider`, `flux:slider.tick`; settings `min="1"`, `max="5"`.
- **Range slider** — tags `flux:slider`; settings `range`.
- **Basic usage** — tags `flux:slider`; settings `range`.
- **Min steps between** — tags `flux:slider`; settings `range`, `step="1"`, `min-steps-between="10"`.
- **Displaying values** — tags `flux:field`, `flux:label`, `flux:slider`; settings `range`, `min="0"`, `max="990"`, `step="10"`, `min-steps-between="10"`, `big-step="100"`.
- **Custom styles** — tags `flux:slider`; settings `track:class="h-5"`, `thumb:class="size-5"`.

**Full page:** `references/source/components/slider.md` (bundled) or [live](https://fluxui.dev/components/slider.md). Read it for exact props, slots, and values.
