# Carousel

- **Availability:** Flux Pro.
- **Use:** Present a sequence of horizontally scrollable slides.
- **Main tags:** `flux:carousel`, `flux:carousel.slide`, `flux:carousel.controls`.
- **Common props:** `arrows`, `arrows:position`, `arrows:class`, `autoplay`, `autoplay:interval`, `indicators`, `disabled`, `fade`, `bleed`, `snap`, `scroll`, `advance`.

**Starter:**

```blade
<flux:carousel><flux:carousel.slide>First slide</flux:carousel.slide><flux:carousel.slide>Second slide</flux:carousel.slide></flux:carousel>
```

## How to customize

- Place each piece of content in a slide and choose dimensions that make the sequence understandable.
- Indicators and arrows expose navigation; autoplay can advance slides on a chosen interval.
- Fade, snap, page advance, control placement, and external controls change the browsing interaction.

## Capabilities

- **Indicators** — tags `flux:carousel`, `flux:carousel.slide`; settings `indicators`.
- **Autoplay** — tags `flux:carousel`; settings `autoplay`, `autoplay:interval="3500"`, `indicators`.
- **External controls** — tags `flux:heading`, `flux:text`, `flux:carousel.controls`, `flux:carousel`, `flux:carousel.slide`; settings `bleed`.
- **Arrow position** — tags `flux:carousel`; settings `arrows:position="inside"`, `arrows:position="overlap"`, `arrows:position="outside"`.
- **Fade** — tags `flux:carousel`; settings `fade`, `bleed`.
- **Page advance** — tags `flux:carousel`; settings `advance="page"`.

## Component API

- **`flux:carousel`** — props: `arrows` (default `true`), `arrows:position` (values `inside`, `overlap`, `outside`; default `inside`), `arrows:class`, `autoplay`, `autoplay:interval` (default `5000`), `indicators` (default `false`), `disabled`, `fade`, `bleed`, `snap` (values `proximity`, `mandatory`; default `proximity`), `scroll` (values `smooth`, `instant`; default `smooth`), `advance` (values `slide`, `page`; default `slide`), `wrap` (values `none`, `rewind`; default `none`), `name`, `track:class`.
- **`flux:carousel.slide`** — props: `class`.
- **`flux:carousel.controls`** — props: `name`.

**Implementation:** Place slides inside `flux:carousel`; configure arrows, indicators, autoplay, snapping, or fade only when needed.

**Current source:** [Flux UI](https://fluxui.dev/components/carousel.md).
