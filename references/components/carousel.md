# Carousel

- **Availability:** Flux Pro.
- **Use:** Present a sequence of horizontally scrollable slides.
- **Main tags:** `flux:carousel`, `flux:carousel.slide`, `flux:carousel.controls`.
- **Common props:** `arrows`, `arrows:position`, `arrows:class`, `autoplay`, `autoplay:interval`, `indicators`, `disabled`, `fade`, `bleed`, `snap`, `scroll`, `advance`.

**Starter:**

```blade
<flux:carousel><flux:carousel.slide>First slide</flux:carousel.slide><flux:carousel.slide>Second slide</flux:carousel.slide></flux:carousel>
```

**Implementation:** Place slides inside `flux:carousel`; configure arrows, indicators, autoplay, snapping, or fade only when needed.

**Current source:** [Flux UI](https://fluxui.dev/components/carousel.md).
