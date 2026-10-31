# File upload

- **Availability:** Flux Pro.
- **Use:** Upload and preview one or more files.
- **Main tags:** `flux:file-upload`, `flux:file-upload.dropzone`, `flux:file-item`, `flux:file-item.remove`.
- **Common props:** `name`, `multiple`, `label`, `description`, `error`, `disabled`, `wire:model`.

**Starter:**

```blade
<flux:file-upload wire:model="files" multiple><flux:file-upload.dropzone /></flux:file-upload>
```

**Implementation:** Bind with Livewire and use a dropzone or file items. Validate file type, size, and storage on the server; upload UI alone is not validation.

**Current source:** [Flux UI](https://fluxui.dev/components/file-upload.md).
