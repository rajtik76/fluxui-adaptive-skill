# Pagination

- **Availability:** Flux (free).
- **Use:** Navigate through a Laravel paginated result set.
- **Main tags:** `flux:pagination`.
- **Common props:** `paginator`, `scroll-to`.

**Starter:**

```blade
<flux:pagination :paginator="$orders" />
```

**Implementation:** Pass a paginator instance to `:paginator`. Use Laravel simple pagination when total counts are expensive.

**Current source:** [Flux UI](https://fluxui.dev/components/pagination.md).
