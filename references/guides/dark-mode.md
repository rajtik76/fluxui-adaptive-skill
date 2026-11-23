# Dark mode

Flux can manage light, dark, and system appearance. Configure the application's Tailwind dark selector and decide whether Flux or the application owns appearance state.

## Setup and ownership

- Import Flux CSS and define the `dark` custom variant against the `.dark` class on an ancestor.
- With `@fluxAppearance` in the layout, Flux handles the root dark class according to the selected or system appearance. Omit that directive only when the application deliberately handles this itself.
- The Alpine utility `$flux.appearance` represents `light`, `dark`, or `system`; `$flux.dark` reflects or changes the current dark state. Outside Alpine, the same state is available through `window.Flux`.

## Controls

A toggle can flip the current state. A dropdown or segmented radio control can expose all three appearance choices. Bind the control to the appearance utility rather than maintaining a second unsynchronized state. If implementing custom state handling, remember to persist preference and respond to changes in the system setting.

**Full page:** `references/source/docs/dark-mode.md` (bundled) or [live](https://fluxui.dev/docs/dark-mode.md).
