# Pagination

- **Availability:** Flux (free).
- **Use:** Navigate through a Laravel paginated result set.
- **Main tags:** `flux:pagination`.
- **Common props:** `paginator`, `scroll-to`.

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

## Component API

- **`flux:pagination`** — props: `paginator`, `scroll-to` (default `body`).

**Implementation:** Pass a paginator instance to `:paginator`. Use Laravel simple pagination when total counts are expensive.

**Current source:** [Flux UI](https://fluxui.dev/components/pagination.md).
