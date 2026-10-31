# Chart

- **Availability:** Flux Pro.
- **Use:** Visualize Livewire data with Flux chart primitives.
- **Main tags:** `flux:chart`, `flux:chart.svg`, `flux:chart.line`, `flux:chart.area`, `flux:chart.point`, `flux:chart.pie`.
- **Common props:** `wire:model`, `value`, `horizontal`, `class`.

**Starter:**

```blade
<flux:chart wire:model="data"><flux:chart.svg><flux:chart.line field="visitors" /></flux:chart.svg></flux:chart>
```

## How to customize

- Provide named data fields and select a line, area, bar, pie, or donut composition inside chart primitives.
- Configure axes, scale, grid, ticks, cursor, tooltip, legend, and summary to make values readable.
- Use field-based colors and number/date formatting deliberately; live data can be bound through Livewire.

## Capabilities

- **Data structure** — Pass an array of named data points via `wire:model` or `:value`; fields supply the series.
- **Line chart** — tags `flux:chart`, `flux:chart.svg`, `flux:chart.line`, `flux:chart.point`, `flux:chart.axis`; settings `field="memory"`, `axis="x"`, `field="date"`, `axis="y"`.
- **Area chart** — tags `flux:chart`, `flux:chart.svg`, `flux:chart.line`, `flux:chart.area`, `flux:chart.axis`; settings `field="stock"`, `curve="none"`, `axis="y"`, `position="right"`, `axis="x"`, `field="date"`.
- **Multiple lines** — tags `flux:chart`, `flux:chart.viewport`, `flux:chart.svg`, `flux:chart.line`, `flux:chart.point`; settings `field="twitter"`, `curve="none"`, `field="facebook"`, `field="instagram"`, `axis="x"`, `field="date"`.
- **Bar chart** — tags `flux:chart`, `flux:chart.svg`, `flux:chart.bar`, `flux:chart.axis`, `flux:chart.axis.tick`; settings `field="revenue"`, `radius="0"`, `axis="x"`, `field="date"`, `axis="y"`.
- **Horizontal charts** — tags `flux:chart`, `flux:chart.svg`, `flux:chart.bar`, `flux:chart.axis`, `flux:chart.axis.tick`; settings `horizontal`, `field="online"`, `radius="4 0"`, `axis="y"`, `field="category"`, `axis="x"`.
- **Grouped bar chart** — tags `flux:chart`, `flux:chart.viewport`, `flux:chart.svg`, `flux:chart.group`, `flux:chart.bar`; settings `field="chrome"`, `field="firefox"`, `field="safari"`, `axis="x"`, `field="year"`, `axis="y"`.
- **Stacked bar chart** — tags `flux:chart`, `flux:chart.viewport`, `flux:chart.svg`, `flux:chart.stack`, `flux:chart.bar`; settings `field="online"`, `field="retail"`, `field="wholesale"`, `radius="4 0"`, `axis="x"`, `field="category"`.
- **Pie chart** — tags `flux:chart`, `flux:chart.viewport`, `flux:chart.svg`, `flux:chart.pie`, `flux:chart.tooltip`; settings `field="value"`, `label-field="label"`.
- **Donut chart** — tags `flux:chart`, `flux:chart.viewport`, `flux:chart.svg`, `flux:chart.pie`, `flux:chart.tooltip`; settings `field="value"`, `label-field="label"`, `inner-radius="60%"`, `radius="4"`.
- **Slice colors** — Pie slice colors follow stable identities; provide a color in data to override the palette.
- **Hover styles** — tags `flux:chart.pie`.
- **Live summary** — tags `flux:card`, `flux:chart`, `flux:chart.summary`, `flux:text`, `flux:heading`; settings `field="sales"`, `field="date"`, `field="yesterday"`.
- **Sparkline** — tags `flux:chart`, `flux:chart.svg`, `flux:chart.line`.
- **Dashboard stat** — tags `flux:card`, `flux:text`, `flux:heading`, `flux:chart`, `flux:chart.svg`.
- **Chart padding** — tags `flux:chart`, `flux:chart.svg`.
- **Axis scale** — tags `flux:chart.axis`; settings `axis="y"`.
- **Axis lines** — tags `flux:chart.svg`, `flux:chart.axis`, `flux:chart.axis.line`; settings `axis="x"`, `axis="y"`.
- **Zero line** — tags `flux:chart.svg`, `flux:chart.zero-line`.
- **Grid lines** — tags `flux:chart.svg`, `flux:chart.axis`, `flux:chart.axis.grid`; settings `axis="x"`, `axis="y"`.
- **Ticks** — tags `flux:chart.svg`, `flux:chart.axis`, `flux:chart.axis.mark`, `flux:chart.axis.tick`; settings `axis="x"`, `axis="y"`.
- **Tick frequency** — tags `flux:chart.axis`; settings `axis="y"`.
- **Tick formatting** — tags `flux:chart.svg`, `flux:chart.axis`, `flux:chart.axis.tick`; settings `axis="x"`, `axis="y"`.
- **Cursor** — tags `flux:chart.svg`, `flux:chart.cursor`.
- **Tooltip** — tags `flux:chart`, `flux:chart.svg`, `flux:chart.tooltip`, `flux:chart.tooltip.heading`, `flux:chart.tooltip.value`; settings `field="date"`, `field="visitors"`, `field="views"`.
- **Legend** — tags `flux:chart`, `flux:chart.viewport`, `flux:chart.svg`, `flux:chart.line`, `flux:chart.legend`; settings `field="visitors"`, `field="views"`.
- **Summary** — tags `flux:chart`, `flux:chart.summary`, `flux:chart.summary.value`, `flux:chart.viewport`; settings `field="visitors"`.
- **Formatting** — Use `:format` options for locale-aware number and date labels.
- **Formatting numbers** — tags `flux:chart.axis`; settings `axis="y"`.
- **Formatting dates** — tags `flux:chart.axis`; settings `axis="x"`, `field="date"`.

## Component API

- **`flux:chart`** — props: `wire:model`, `value`, `horizontal`; CSS: `class`.
- **`flux:chart.line`** — props: `field`, `curve` (values `smooth`, `none`); CSS: `class`.
- **`flux:chart.area`** — props: `field`, `curve` (values `smooth`, `none`); CSS: `class`.
- **`flux:chart.point`** — props: `field`; CSS: `class`.
- **`flux:chart.pie`** — props: `field` (default `value`), `label-field`, `inner-radius` (default `0`), `radius` (default `0`); CSS: `class`.
- **`flux:chart.axis`** — props: `axis` (values `x`, `y`), `field`, `format`.
- **`flux:chart.axis.mark`** — props: `position` (values `top`, `bottom`, `left`, `right`); CSS: `class`.
- **`flux:chart.axis.line`** — CSS: `class`.
- **`flux:chart.axis.grid`** — CSS: `class`.
- **`flux:chart.axis.tick`** — props: `format`; CSS: `class`.
- **`flux:chart.zero-line`** — CSS: `class`.
- **`flux:chart.tooltip`** — props: `field`, `format`.
- **`flux:chart.tooltip.heading`** — props: `field`, `format`.
- **`flux:chart.tooltip.value`** — props: `field`, `format`, `label`, `label-field`.
- **`flux:chart.tooltip.indicator`** — CSS: `class`.
- **`flux:chart.cursor`** — CSS: `class`.
- **`flux:chart.summary.value`** — props: `field`, `fallback`, `format`.
- **`flux:chart.legend`** — props: `field`, `label`, `format`.

**Implementation:** Bind an array of named data points; nest `flux:chart.svg` and a line, area, bar, or other plot. Plot `field` names must match data keys.

**Current source:** [Flux UI](https://fluxui.dev/components/chart.md).
