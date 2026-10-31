# Time picker

- **Availability:** Flux Pro.
- **Use:** Choose one or more clock times.
- **Main tags:** `flux:time-picker`.
- **Common props:** `wire:model`, `value`, `type`, `multiple`, `time-format`, `interval`, `min`, `max`, `unavailable`, `open-to`, `label`, `description`.

**Starter:**

```blade
<flux:time-picker wire:model="time" />
```

## How to customize

- Bind a time value; choose dropdown or typed-input presentation.
- Multiple selection, intervals, and 12/24-hour display fit different scheduling tasks.
- Limit min/max or unavailable times and choose the initial opening time and locale.

## Capabilities

- **Basic usage** — tags `flux:time-picker`.
- **Input trigger** — tags `flux:time-picker`.
- **Without dropdown** — tags `flux:time-picker`.
- **Multiple times** — tags `flux:time-picker`; settings `multiple`.
- **Time format** — tags `flux:time-picker`; settings `time-format="12-hour"`, `time-format="24-hour"`.
- **Interval** — tags `flux:time-picker`; settings `interval="60"`.
- **Min/max times** — tags `flux:time-picker`; settings `min="09:00"`, `max="17:00"`.
- **Unavailable times** — tags `flux:time-picker`; settings `unavailable`.
- **Open to** — tags `flux:time-picker`; settings `open-to="10:00"`.
- **Localization** — tags `flux:time-picker`; settings `locale="ja-JP"`.

## Component API

- **`flux:time-picker`** — props: `wire:model`, `value`, `type` (values `input`, `button`; default `button`), `multiple` (default `false`), `time-format` (values `auto`, `12-hour`, `24-hour`), `interval` (default `30`), `min`, `max`, `unavailable`, `open-to`, `label`, `description`, `description:trailing`, `badge`, `placeholder`, `size` (values `sm`, `xs`), `clearable`, `disabled`, `invalid`, `locale`.

**Implementation:** Single values use `H:i`; a typed trigger or interval list can suit the task. Check multiple mode and time limits in the live page.

**Current source:** [Flux UI](https://fluxui.dev/components/time-picker.md).
