# File upload

- **Availability:** Flux Pro.
- **Use:** Upload and preview one or more files.
- **Main tags:** `flux:file-upload`, `flux:file-upload.dropzone`, `flux:file-item`, `flux:file-item.remove`.

**Starter:**

```blade
<flux:file-upload wire:model="files" multiple><flux:file-upload.dropzone /></flux:file-upload>
```

## How to customize

- Bind one uploaded file or an array of files to a Livewire property.
- A dropzone can show a heading, guidance, previews, and upload progress; inline layout fits compact forms.
- Use custom uploader composition when necessary, but keep server-side file validation and storage in Livewire.

## Capabilities

- **Inline layout** — tags `flux:file-upload`, `flux:file-upload.dropzone`, `flux:file-item`, `flux:file-item.remove`; settings `multiple`, `heading`, `text`, `inline`.
- **Progress indicator** — tags `flux:file-upload`, `flux:file-upload.dropzone`; settings `multiple`, `heading`, `text`, `with-progress`, `inline`.
- **Disabled state** — tags `flux:file-upload`, `flux:file-upload.dropzone`; settings `multiple`, `disabled`, `heading`, `text`, `inline`.
- **Custom uploader** — tags `flux:file-upload`, `flux:icon`.
- **Livewire integration** — Bind uploads to Livewire properties with `wire:model`; handle validation and storage in the component.
- **Single file upload** — Bind one upload to a single property and manage its preview/removal.
- **Multiple files upload** — Bind an array property and enable `multiple` for several files.

**Full page:** `references/source/components/file-upload.md` (bundled) or [live](https://fluxui.dev/components/file-upload.md). Read it for exact props, slots, and values.
