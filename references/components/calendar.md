# Calendar

- **Availability:** Flux Pro.
- **Use:** Select dates directly in a calendar view.
- **Main tags:** `flux:calendar`.

**Starter:**

```blade
<flux:calendar wire:model="selectedDate" />
```

## How to customize

- Use single, multiple, or range mode according to the data being collected; bind dates to a Livewire property.
- Constrain selection with min/max and unavailable dates. Control today shortcut, month navigation, week numbering, start day, and locale.
- For ranges, `DateRange` offers an object with Carbon-period behavior that can be reused in queries.

## Capabilities

- **Basic Usage** — tags `flux:calendar`.
- **Multiple dates** — tags `flux:calendar`; settings `multiple`.
- **Date range** — tags `flux:calendar`; settings `mode="range"`.
- **Range Configuration** — tags `flux:calendar`; settings `mode="range"`, `min-range="3"`, `max-range="10"`, `months="2"`.
- **Size** — tags `flux:calendar`; settings `size="xl"`.
- **Static** — tags `flux:calendar`; settings `static`.
- **Min/max dates** — tags `flux:calendar`; settings `max`.
- **Unavailable dates** — tags `flux:calendar`; settings `unavailable`.
- **With today shortcut** — tags `flux:calendar`; settings `with-today`.
- **Selectable header** — tags `flux:calendar`; settings `selectable-header`.
- **Fixed weeks** — tags `flux:calendar`.
- **Start day** — tags `flux:calendar`; settings `start-day="1"`.
- **Open to** — tags `flux:calendar`; settings `open-to`.
- **Week numbers** — tags `flux:calendar`; settings `week-numbers`.
- **Localization** — tags `flux:calendar`; settings `locale="ja-JP"`.
- **The DateRange object** — tags `flux:calendar`.
- **Instantiation** — Construct a `DateRange` with its start and end dates.
- **Persisting to the session** — Livewire session state can retain a `DateRange`.
- **Using with Eloquent** — A `DateRange` can supply bounds to Eloquent `whereBetween()`.
- **Available methods** — `DateRange` extends `CarbonPeriod` and exposes its date-range methods.

**Full page:** `references/source/components/calendar.md` (bundled) or [live](https://fluxui.dev/components/calendar.md). Read it for exact props, slots, and values.
