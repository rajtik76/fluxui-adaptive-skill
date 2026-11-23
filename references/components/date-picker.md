# Date picker

- **Availability:** Flux Pro.
- **Use:** Choose a date or date interval from an overlay calendar.
- **Main tags:** `flux:date-picker`, `flux:date-picker.input`, `flux:date-picker.button`.

**Starter:**

```blade
<flux:date-picker wire:model="date" />
```

## How to customize

- Choose a calendar button or input trigger, and bind a single date or date range.
- Range presets and input pairs speed up common reporting periods; min/max and unavailable dates restrict invalid choices.
- Customize navigation, week layout, locale, and opening month. The `DateRange` object supports range state and queries.

## Capabilities

- **Basic usage** — tags `flux:date-picker`.
- **Input trigger** — tags `flux:date-picker`.
- **Range picker** — tags `flux:date-picker`; settings `mode="range"`.
- **Range limits** — tags `flux:date-picker`; settings `mode="range"`, `min-range="3"`.
- **Range with inputs** — tags `flux:date-picker`, `flux:date-picker.input`; settings `mode="range"`, `variant="custom"`.
- **Presets** — tags `flux:date-picker`; settings `mode="range"`, `with-presets`.
- **Available presets** — Built-in keys cover common relative ranges such as today, this week, and last month.
- **All time** — tags `flux:date-picker`; settings `mode="range"`, `presets="... allTime"`.
- **Custom range preset** — tags `flux:date-picker`; settings `mode="range"`, `presets="... custom"`.
- **Unavailable dates** — tags `flux:date-picker`; settings `unavailable`.
- **With today shortcut** — tags `flux:date-picker`; settings `with-today`.
- **Selectable header** — tags `flux:date-picker`; settings `selectable-header`.
- **Fixed weeks** — tags `flux:date-picker`.
- **Start day** — tags `flux:date-picker`; settings `start-day="1"`.
- **Open to** — tags `flux:date-picker`; settings `open-to`.
- **Week numbers** — tags `flux:date-picker`; settings `week-numbers`.
- **Localization** — tags `flux:date-picker`; settings `locale="ja-JP"`.
- **The DateRange object** — tags `flux:calendar`.
- **Instantiation** — Construct a `DateRange` from start and end dates.
- **Persisting to the session** — A `DateRange` can be retained with Livewire session state.
- **Using with Eloquent** — Use range bounds in an Eloquent `whereBetween()` query.
- **Available methods** — `DateRange` extends `CarbonPeriod` and exposes its methods.
- **Range presets** — The bound range can carry a preset key alongside its dates.

**Full page:** `references/source/components/date-picker.md` (bundled) or [live](https://fluxui.dev/components/date-picker.md). Read it for exact props, slots, and values.
