# Pagination

- **Availability:** Flux (free).
- **Use:** Navigate through a Laravel paginated result set.
- **Main tags:** `flux:pagination`.

**Starter:**

```blade
<flux:pagination :paginator="$orders" />
```

## How to customize

- Pass a Laravel paginator rather than building page links manually.
- Use a simple paginator for large result sets when counting totals is expensive.
- Choose the scroll target so navigation returns users to the relevant list.

## Capabilities

- **Simple paginator** — tags `flux:pagination`.
- **Large result set** — tags `flux:pagination`.
- **Scroll to top** — tags `flux:pagination`; settings `scroll-to`.

**Full page:** `references/source/components/pagination.md` (bundled) or [live](https://fluxui.dev/components/pagination.md). Read it for exact props, slots, and values.
