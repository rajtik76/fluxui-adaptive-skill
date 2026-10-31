# Principles

Use these principles when choosing between a Flux component, composing smaller Flux pieces, and writing ordinary Blade or CSS.

- **Simple defaults:** Start with the shortest component structure that expresses the task. Move to composition when the default hides a needed control.
- **Composition:** Build more complex UI from compatible primitives instead of assuming each use case needs a monolithic component.
- **Consistent names:** Related components tend to reuse familiar props and child naming patterns; verify the actual reference before applying an analogy.
- **Browser behavior:** Native browser capabilities, including search and semantic controls, can be part of the component's behavior.
- **CSS responsibilities:** Flux supplies the component appearance while the application commonly supplies surrounding spacing and layout. Use project Tailwind conventions for margins and placement.
- **Friendly brevity:** Keep UI labels and component structure clear without piling on decorative wrappers.

These are design preferences, not a substitute for a component's documented API.

**Current source:** [Flux UI principles](https://fluxui.dev/docs/principles.md).
