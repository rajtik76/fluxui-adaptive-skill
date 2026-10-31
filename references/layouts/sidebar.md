# Sidebar layout

Use a persistent side navigation when the application has many destinations or nested groups. The official layout shows a sidebar, profile area, a mobile header, and a main content region. Keep only the pieces the product needs.

## Structure

```blade
<flux:sidebar sticky collapsible="mobile">
    <flux:sidebar.header>
        <flux:sidebar.brand href="/" name="App" />
    </flux:sidebar.header>
    <flux:sidebar.nav>
        <flux:sidebar.item href="/dashboard" current>Dashboard</flux:sidebar.item>
    </flux:sidebar.nav>
</flux:sidebar>

<flux:main>
    <!-- Page content -->
</flux:main>
```

Load Flux appearance and scripts as described in [Installation](../guides/installation.md). On mobile, pair the collapsible sidebar with a toggle in a compact header.

## Customization and API

- `flux:sidebar` supports sticky positioning, collapsible modes, a breakpoint, stashing, and persistence. Choose these according to responsive behavior rather than enabling all at once.
- The sidebar family includes header, brand, search, nav, item, group, spacer, profile, collapse, and toggle components.
- Items accept destination, icon, badge, current state, and tooltip. Groups can have headings and be expandable or initially expanded.
- `flux:main inset` gives the content a contained panel; a secondary top header can hold context actions or navigation.
- Use [Header layout](header.md) when a top bar is the primary shell.

**Current source:** [Flux UI sidebar layout](https://fluxui.dev/layouts/sidebar.md).
