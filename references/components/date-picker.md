# Date picker

- **Availability:** Flux Pro.
- **Use:** Choose a date or date interval from an overlay calendar.
- **Main tags:** `flux:date-picker`, `flux:date-picker.input`, `flux:date-picker.button`.
- **Common props:** `wire:model`, `value`, `type`, `mode`, `min-range`, `max-range`, `min`, `max`, `unavailable`, `open-to`, `force-open-to`, `months`.

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

## Component API

- **`flux:date-picker`** — props: `wire:model`, `value`, `type` (values `button`, `input`), `mode` (values `single`, `range`), `min-range`, `max-range`, `min`, `max`, `unavailable`, `open-to`, `force-open-to` (default `false`), `months` (default `1`), `label`, `description`, `description:trailing`, `badge`, `placeholder`, `size` (values `sm`, `default`, `lg`, `xl`, `2xl`), `start-day` (values `0`, `6`), `week-numbers`, `selectable-header`, `with-today`, `with-inputs` (values `custom`, `native`), `with-confirmation`, `with-presets`, `presets` (default `today yesterday thisWeek last7Days thisMonth yearToDate allTime`), `clearable`, `disabled`, `invalid`, `locale`; slots: `trigger`.
- **`flux:date-picker.input`** — props: `variant` (values `custom`, `native`), `label`, `description`, `placeholder`, `clearable`, `disabled`, `invalid`, `size` (values `sm`, `xs`).
- **`flux:date-picker.button`** — props: `placeholder`, `size` (values `sm`, `xs`), `clearable`, `disabled`, `invalid`.

**Implementation:** A single date uses `Y-m-d`; `mode="range"` enables intervals. Check limits, unavailable dates, presets, and trigger variants in the live page when needed.

**Current source:** [Flux UI](https://fluxui.dev/components/date-picker.md).
