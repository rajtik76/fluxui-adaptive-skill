# Header layout

Use a horizontal header when the application has a small set of primary destinations and content should span the page width. The official layout combines a header, navigation, profile actions, a mobile sidebar, and a main region; adapt those pieces to the actual product.

## Structure

```blade
<flux:header container>
    <flux:brand href="/" name="App" />
    <flux:navbar>
        <flux:navbar.item href="/dashboard" current>Dashboard</flux:navbar.item>
    </flux:navbar>
</flux:header>

<flux:main container>
    <!-- Page content -->
</flux:main>
```

The layout should also load the assets described in [Installation](../guides/installation.md). Use semantic current navigation state, responsive visibility, and a mobile menu or sidebar as the number of destinations grows.

## Customization and API

- `flux:header` supports `sticky` for a persistent top bar and `container` for a constrained content width.
- `flux:sidebar.toggle` can open the mobile sidebar; its icon and inset can be adjusted.
- `flux:main` supports `container` and `inset`. Inset places content in a bordered panel on larger screens while retaining usable scrolling on smaller screens.
- A secondary sidebar can accompany the header when the application needs another navigation level. Keep primary and secondary destinations distinct.
- Use the [Sidebar layout](sidebar.md) for a navigation-first shell instead.

**Full page:** `references/source/layouts/header.md` (bundled) or [live](https://fluxui.dev/layouts/header.md).
