# Datetime picker

- **Availability:** Flux Pro.
- **Use:** Choose a date and time together for a scheduled event.
- **Main tags:** `flux:datetime-picker`, `flux:datetime-picker.button`.

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

**Full page:** `references/source/components/datetime-picker.md` (bundled) or [live](https://fluxui.dev/components/datetime-picker.md). Read it for exact props, slots, and values.
