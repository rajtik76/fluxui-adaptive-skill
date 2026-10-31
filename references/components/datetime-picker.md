# Datetime picker

- **Availability:** Flux Pro.
- **Use:** Choose a date and time together for a scheduled event.
- **Main tags:** `flux:datetime-picker`, `flux:datetime-picker.button`.
- **Common props:** `wire:model`, `value`, `name`, `mode`, `placeholder`, `size`, `time`, `interval`, `time-format`, `min`, `max`, `min-time`.

**Starter:**

```blade
<flux:datetime-picker wire:model="startsAt" />
```

## How to customize

- Bind a single local datetime or a start/end range; the value format includes both date and time.
- Use list intervals or direct time input, then configure defaults, limits, unavailable slots, and confirmation behavior.
- The value is a wall-clock time, so application code must handle user timezone conversion. `DateTimeRange` supplies typed range endpoints.

## Capabilities

- **Basic usage** — tags `flux:datetime-picker`.
- **Range picker** — tags `flux:datetime-picker`; settings `mode="range"`.
- **Range limits** — tags `flux:datetime-picker`; settings `mode="range"`, `max-range="7"`.
- **Time input** — tags `flux:datetime-picker`; settings `time="input"`.
- **Interval** — tags `flux:datetime-picker`; settings `interval="15"`.
- **Default time** — tags `flux:datetime-picker`; settings `default-time="09:00"`.
- **Min/max** — tags `flux:datetime-picker`; settings `min="now"`, `max`.
- **Min/max times** — tags `flux:datetime-picker`; settings `min="now"`, `min-time="09:00"`, `max-time="17:00"`.
- **Unavailable dates and times** — tags `flux:datetime-picker`; settings `unavailable`.
- **Time format** — tags `flux:datetime-picker`; settings `time-format="12-hour"`, `time-format="24-hour"`.
- **Clearable** — tags `flux:datetime-picker`; settings `clearable`.
- **With confirmation** — tags `flux:datetime-picker`; settings `with-confirmation`.
- **Custom trigger** — tags `flux:datetime-picker`, `flux:button`.
- **Calendar options** — tags `flux:datetime-picker`; settings `with-today`, `selectable-header`, `week-numbers`.
- **Open to** — tags `flux:datetime-picker`; settings `open-to="2026-12-01T09:00"`.
- **Localization** — tags `flux:datetime-picker`; settings `locale="fr-FR"`.
- **Separate date and time** — tags `flux:date-picker`, `flux:time-picker`.
- **Timezones** — Values are local wall-clock times; convert to the user timezone explicitly when the application needs it.
- **The DateTimeRange object** — Bind a `Flux\DateTimeRange` for a range with Carbon start and end values.

## Component API

- **`flux:datetime-picker`** — props: `wire:model`, `value`, `name`, `mode` (values `single`, `range`), `placeholder` (default `Select a date and time`), `size` (values `xs`, `sm`, `lg`, `xl`, `2xl`), `time` (values `list`, `input`), `interval` (default `30`), `time-format` (values `auto`, `12-hour`, `24-hour`), `min`, `max`, `min-time`, `max-time`, `unavailable`, `default-time`, `min-range`, `max-range`, `months` (default `1`), `with-confirmation`, `clearable`, `with-today`, `selectable-header`, `week-numbers`, `start-day` (values `0`, `6`), `fixed-weeks`, `open-to`, `locale`, `label`, `description`, `description:trailing`, `badge`, `disabled`, `invalid`; slots: `trigger`; events: `open`, `close`, `clear`.
- **`flux:datetime-picker.button`** — props: `placeholder`, `size` (values `sm`, `xs`), `clearable`, `invalid`.

**Implementation:** Single values use `Y-m-d\TH:i`; `mode="range"` accepts start/end datetimes. Configure time input, interval, limits, and unavailable slots as needed.

**Current source:** [Flux UI](https://fluxui.dev/components/datetime-picker.md).
