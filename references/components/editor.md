# Rich text editor

- **Availability:** Flux Pro.
- **Use:** Edit formatted text in a Livewire form.
- **Main tags:** `flux:editor`, `flux:editor.toolbar`, `flux:editor.button`, `flux:editor.content`.

**Starter:**

```blade
<flux:editor wire:model="content" label="Content" />
```

## How to customize

- Bind rich-text content and choose a toolbar suited to the operations users need.
- Toolbar items can be reordered or replaced; shortcuts and Markdown-like typing accelerate formatting.
- Localize controls or register Tiptap extensions through the documented editor event when built-in behavior is insufficient.

## Capabilities

- **Toolbar** — Toolbar controls can be customized and remain keyboard and screen-reader accessible.
- **Configuring items** — tags `flux:editor`; settings `toolbar`.
- **Custom items** — Place custom toolbar item views under `resources/views/flux/editor` and reference their names in toolbar configuration.
- **Customization** — tags `flux:editor`, `flux:editor.toolbar`, `flux:editor.heading`, `flux:editor.separator`, `flux:editor.bold`; settings `icon`, `tooltip="More"`.
- **Height** — tags `flux:editor`.
- **Shortcut keys** — Tiptap shortcuts cover common heading and formatting actions.
- **Markdown syntax** — Typing common Markdown markers can apply rich-text formatting; the saved content is still rich text.
- **Localization** — Translate editor tooltip and accessibility labels through application language files.
- **Extensions** — Tiptap extensions add editor behavior; some are bundled and enabled by default.
- **Set up listener** — Listen for the `flux:editor` event in the layout or JavaScript entry point.
- **Registering extensions** — Call `registerExtensions` from the editor event to add Tiptap extensions.
- **Enabling extensions** — Call `enableExtension` to activate a bundled extension.
- **Disabling extensions** — Call `disableExtension` with an extension name to turn it off.
- **Accessing the instance** — Use the editor event `init` callback to access the underlying Tiptap instance.

**Full page:** `references/source/components/editor.md` (bundled) or [live](https://fluxui.dev/components/editor.md). Read it for exact props, slots, and values.
