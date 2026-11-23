> [!PRO]
> This component is only available in the Pro version of Flux.

# Datetime picker

Let users pick a date and a time together from a single field. Perfect for scheduling events, publishing posts, setting reminders, or booking a window of time.

> [!TIP]
> Only need a date or only need a time? Reach for the [date picker](https://fluxui.dev/components/date-picker) or [time picker](https://fluxui.dev/components/time-picker) instead.

```blade
<flux:datetime-picker />
```

### Basic usage

Choose a day from the calendar and a time from the list beside it. Picking a time closes the picker, and changing just the date updates the value straight away. On mobile, selections are confirmed with a "Select" button instead.

Set the initial value using the `value` prop with a `Y-m-d\TH:i` formatted string (the same format as a native `datetime-local` input):

```html
<flux:datetime-picker value="{{ now()->addDays(5)->setTime(10, 30)->format('Y-m-d\TH:i') }}" />
```

You can also bind the selection to a Livewire property using `wire:model`:

```html
<flux:datetime-picker wire:model="startsAt" />
```

Now you can access the selected datetime from your Livewire component using either a `Carbon` instance or a `Y-m-d\TH:i` formatted string:

```php
<?php

use Illuminate\Support\Carbon;
use Livewire\Component;
use App\Models\Event;

class CreateEvent extends Component {
    public ?Carbon $startsAt;

    public function save()
    {
        Event::create([
            // ...
            'starts_at' => $this->startsAt,
        ]);

        // ...
    }
}
```

## Range picker

Select a start and an end datetime for things like event schedules, maintenance windows, or bookings. Each end of the range gets its own time, and the range is applied when "Select range" is pressed.

```blade
<flux:datetime-picker mode="range" />
```

Set the initial range using the `value` prop with a start and end datetime separated by a forward slash:

```html
<flux:datetime-picker mode="range" value="{{ now()->addDays(5)->setTime(9, 0)->format('Y-m-d\TH:i') }}/{{ now()->addDays(10)->setTime(17, 0)->format('Y-m-d\TH:i') }}" />
```

You can also bind the selection to a Livewire property using `wire:model`:

```html
<flux:datetime-picker mode="range" wire:model="schedule" />
```

Now you can access the selected range from your Livewire component as an associative array of `Y-m-d\TH:i` formatted strings:

```php
<?php

use Livewire\Component;

class Maintenance extends Component {
    public array $schedule;

    public function mount() {
        $this->schedule = [
            'start' => now()->addDay()->setTime(22, 0)->format('Y-m-d\TH:i'),
            'end' => now()->addDays(2)->setTime(2, 0)->format('Y-m-d\TH:i'),
        ];
    }
}
```

Alternatively, you can use the specialized `DateTimeRange` object, which gives you `Carbon` instances for the start and end:

```php
<?php

use Livewire\Component;
use Flux\DateTimeRange;

class Maintenance extends Component {
    public ?DateTimeRange $schedule;

    public function mount() {
        $this->schedule = new DateTimeRange(now()->addDay()->setTime(22, 0), now()->addDays(2)->setTime(2, 0));
    }
}
```

[Check out everything you can do with the `DateTimeRange` object ->](#the-datetimerange-object)

Ranges that start and end on the same day collapse the date in the trigger, for example "Oct 22, 2:00 – 4:30 PM". A range whose end isn't after its start can't be selected.

## Range limits

Limit how many days a range can span using the `min-range` and `max-range` props. Both count days, including the start and end days.

```blade
<flux:datetime-picker mode="range" max-range="7" />
```

## Time input

By default, times are chosen from a list in fixed intervals. When users need to enter an exact time down to the minute, set `time="input"` to use a time input instead. The input still has a dropdown of suggested times.

```blade
<flux:datetime-picker time="input" />
```

This works for ranges too:

```blade
<flux:datetime-picker mode="range" time="input" />
```

## Interval

Set the number of minutes between each time in the list using the `interval` prop. The default is 30 minutes.

```blade
<flux:datetime-picker interval="15" />
```

## Default time

When most selections share a time, set it with the `default-time` prop. It's filled in as soon as a date is picked, so users only need to choose a date. They can still pick a different time.

```blade
<flux:datetime-picker default-time="09:00" />
```

For ranges, pass a start and end time separated by a forward slash:

```html
<flux:datetime-picker mode="range" default-time="09:00/17:00" />
```

## Min/max

Restrict the selectable range using the `min` and `max` props. Dates outside the range are disabled in the calendar, and on the first and last allowed days, times outside the range are disabled too.

```blade
<flux:datetime-picker min="now" max="{{ now()->addWeeks(2)->setTime(17, 0)->format('Y-m-d\TH:i') }}" />
```

Both props accept a datetime (`Y-m-d\TH:i`), a date (`Y-m-d`), or one of these shortcuts:

```html
<!-- Prevent selecting anything before this exact moment... -->
<flux:datetime-picker min="now" />

<!-- Prevent selecting any day before today (any time today is fine)... -->
<flux:datetime-picker min="today" />
```

> These restrictions only apply in the browser. Always validate the submitted value on the server as well.

## Min/max times

Limit the times of day that can be picked, on every date, using the `min-time` and `max-time` props. Times outside the window aren't shown at all. Combine them with `min` and `max` for things like "any future time between 9 AM and 5 PM".

```blade
<flux:datetime-picker min="now" min-time="09:00" max-time="17:00" />
```

## Unavailable dates and times

Block out holidays, breaks, or already-booked slots by passing a comma-separated list to the `unavailable` prop. It accepts three kinds of entries, and you can mix them freely.

```blade
<flux:datetime-picker unavailable="2026-12-25, 12:00-13:00, 2026-10-14T10:00, 2026-10-14T15:00-16:00" />
```

| Entry | Example | Blocks |
| --- | --- | --- |
| A date | `2026-12-25` | That whole day |
| A time or range of times | `12:00`, `12:00-13:00` | Those times on every day |
| A datetime or range on one day | `2026-10-14T10:00`, `2026-10-14T15:00-16:00` | Those times on that day only |

Ranges include both ends, so `12:00-13:00` blocks 1:00 PM too. Use `12:00-12:59` to leave it available.

You can also pass an array, including `Carbon` instances, which are treated as single slots. This makes blocking out existing bookings easy:

```blade
<flux:datetime-picker
    wire:model="startsAt"
    :unavailable="$bookings->pluck('starts_at')"
/>
```

## Time format

By default, times are shown in the 12 or 24-hour format of the user's locale. Override this by setting `time-format` to `12-hour` or `24-hour`.

```blade
<flux:datetime-picker time-format="12-hour" />
<flux:datetime-picker time-format="24-hour" />
```

## Clearable

Show a button in the trigger for clearing the selection by adding the `clearable` prop.

```blade
<flux:datetime-picker clearable />
```

## With confirmation

Require users to press "Select" before the value changes by adding the `with-confirmation` prop. Pressing "Cancel", hitting escape, or clicking away discards the selection. Ranges and the `time="input"` variant always confirm, since they don't have a natural last step.

```blade
<flux:datetime-picker with-confirmation />
```

## Custom trigger

Use your own trigger by passing a button to the `trigger` slot.

```blade
<flux:datetime-picker wire:model="sendAt">
    <x-slot name="trigger">
        <flux:button icon="calendar-days">Schedule</flux:button>
    </x-slot>
</flux:datetime-picker>
```

## Calendar options

The calendar inside the datetime picker supports the same options as the [date picker](https://fluxui.dev/components/date-picker), including `with-today`, `selectable-header`, `week-numbers`, `start-day`, and `fixed-weeks`.

```blade
<flux:datetime-picker with-today selectable-header week-numbers />
```

## Open to

When nothing is selected, the picker opens to the current month with the time list scrolled to the current time. Change this with the `open-to` prop, which accepts a datetime, a date, or just a time.

```blade
<flux:datetime-picker open-to="2026-12-01T09:00" />
```

Pass only a time to open to today's month with the list scrolled to that time:

```html
<flux:datetime-picker open-to="09:00" />
```

## Localization

By default, the datetime picker uses the browser's locale (e.g. `navigator.language`) for month names, weekdays, date formats, and the 12 or 24-hour clock.

Override this by setting the `locale` prop to any valid locale string (e.g. `fr` for French, `ja-JP` for Japanese):

```blade
<flux:datetime-picker locale="fr-FR" />
```

The `locale` prop only affects how dates and times are formatted. Text like "Time", "Cancel", and "Select" is passed through Laravel's `__()` helper, so translate it by adding the following keys to one of your app's lang files. Here's an example for French:

```json
// lang/fr.json

{
    "Select a date and time": "Sélectionnez une date et une heure",
    "Select a date and time range": "Sélectionnez une période",
    "Clear date and time": "Effacer la date et l'heure",
    "Time": "Heure",
    "Start": "Début",
    "End": "Fin",
    "End must be after start": "La fin doit être après le début",
    "Cancel": "Annuler",
    "Select": "Sélectionner",
    "Select range": "Sélectionner la période",
    "Previous month": "Mois précédent",
    "Next month": "Mois suivant",
    "Today": "Aujourd'hui"
}
```

## Separate date and time

If you'd rather keep the date and time as separate fields, place a date picker and a time picker side by side.

```blade
<div class="flex gap-2">
    <flux:date-picker wire:model="date" class="flex-1" />
    <flux:time-picker wire:model="time" class="w-40" />
</div>
```

## Timezones

The datetime picker works with "wall-clock" times and doesn't convert between timezones. The value `2026-10-14T10:30` simply means 10:30 AM on October 14th, the same way a native `datetime-local` input does.

When you bind to a `Carbon` property, Livewire sends the datetime in the property's timezone and parses the selected value back in your application's timezone. A `DateTimeRange` keeps the timezone it was created in, so new selections are read back in that same timezone.

If your users are in different timezones, convert to and from their timezone yourself:

```php
<?php

use Illuminate\Support\Carbon;
use Livewire\Component;

class ScheduleCall extends Component {
    public ?string $startsAt = null;

    public function save()
    {
        $startsAt = Carbon::parse($this->startsAt, auth()->user()->timezone)->utc();

        // ...
    }
}
```

## The DateTimeRange object

Flux provides a `Flux\DateTimeRange` object for datetime ranges. Like the date picker's `DateRange`, it extends the native `CarbonPeriod` class, but it keeps the time of day for both ends.

Type hint a Livewire property as a `DateTimeRange` and bind it with `wire:model`:

```php
<?php

use Livewire\Component;
use Flux\DateTimeRange;

class Maintenance extends Component {
    public ?DateTimeRange $window;

    public function mount() {
        $this->window = new DateTimeRange(now()->setTime(22, 0), now()->addDay()->setTime(2, 0));
    }
}
```

```html
<flux:datetime-picker mode="range" wire:model="window" />
```

Get the start and end as `Carbon` instances:

```php
$window->start(); // Carbon...
$window->end(); // Carbon...

$window->hasStart();
$window->hasEnd();
```

Use it anywhere a `CarbonPeriod` is accepted, such as Eloquent's `whereBetween()`:

```php
$deploys = Deploy::whereBetween('deployed_at', $this->window)->get();
```

You can also pass a `DateTimeRange` straight to the `value` prop:

```blade
<flux:datetime-picker mode="range" :value="$window" />
```

Like the picker itself, a `DateTimeRange` bound with `wire:model` is precise to the minute, so seconds are dropped. And because it's a `CarbonPeriod`, iterating over it steps through one day at a time from the start.

## Related

- [Date picker](https://fluxui.dev/components/date-picker) - Allow users to select dates or date ranges
- [Time picker](https://fluxui.dev/components/time-picker) - Allow users to select specific times
- [Calendar](https://fluxui.dev/components/calendar) - Displays a calendar interface for selecting dates

## Reference

### flux:datetime-picker

**Prop:**

- `wire:model` - Binds the datetime picker to a Livewire property. See the [wire:model documentation](https://livewire.laravel.com/docs/wire-model) for more information.
- `value` - Selected datetime. Format depends on `mode`: a single datetime (`Y-m-d\TH:i`) or a range (`Y-m-d\TH:i/Y-m-d\TH:i`). Also accepts `Carbon` instances and `DateTimeRange` objects.
- `name` - Name of the hidden inputs used for native form submission. Ranges submit `name[start]` and `name[end]`.
- `mode` - Selection mode. Options: `single` (default), `range`.
- `placeholder` - Placeholder text displayed when nothing is selected. Default: `Select a date and time` (or `Select a date and time range`).
- `size` - Size of the trigger and calendar day cells. Options: `xs`, `sm`, `lg`, `xl`, `2xl`. `sm` and `xs` shrink the trigger, `sm` also shrinks the day cells, and `lg`, `xl`, and `2xl` enlarge the day cells.
- `time` - How times are chosen. Options: `list` (default), `input`.
- `interval` - Minutes between each time in the list. Default: `30`.
- `time-format` - Time format. Options: `auto` (default), `12-hour`, `24-hour`.
- `min` - Earliest selectable datetime. Accepts a datetime, a date, a `Carbon` instance, `now`, or `today`.
- `max` - Latest selectable datetime. Accepts a datetime, a date, a `Carbon` instance, `now`, or `today`.
- `min-time` - Earliest time of day that can be selected on any date (`H:i`).
- `max-time` - Latest time of day that can be selected on any date (`H:i`).
- `unavailable` - Comma-separated list (or array) of unavailable dates (`Y-m-d`), daily times (`H:i` or `H:i-H:i`), and datetime slots (`Y-m-d\TH:i` or `Y-m-d\TH:i-H:i`).
- `default-time` - Time filled in when a date is picked (`H:i`). For ranges, a start and end time separated by a forward slash (`H:i/H:i`).
- `min-range` - Minimum number of days a range can span. Only applies when `mode` is `range`.
- `max-range` - Maximum number of days a range can span. Only applies when `mode` is `range`.
- `months` - Number of months to display. Default: `1` for single mode, `2` for range mode.
- `with-confirmation` - Requires pressing "Select" to apply the selection. Always on for ranges, `time="input"`, and on mobile.
- `clearable` - Displays a clear button in the trigger when a datetime is selected.
- `with-today` - Displays a button that navigates the calendar to today.
- `selectable-header` - Displays month and year dropdowns for quick navigation.
- `week-numbers` - Displays week numbers in the calendar.
- `start-day` - Day of the week the calendar starts on. Options: `0` (Sunday) to `6` (Saturday). Default: based on the locale.
- `fixed-weeks` - Always displays six weeks in each month, so the calendar height doesn't change.
- `open-to` - Datetime, date, time, or `Carbon` instance the picker opens to when nothing is selected. Default: now.
- `locale` - Locale used for formatting. Examples: `fr`, `en-US`, `ja-JP`. Default: the browser's locale.
- `label` - Label text displayed above the datetime picker. When provided, wraps the component in a `flux:field` with an adjacent `flux:label`.
- `description` - Help text displayed above the datetime picker. When provided alongside `label`, appears between the label and the datetime picker within the `flux:field` wrapper.
- `description:trailing` - The description provided will be displayed below the datetime picker instead of above it.
- `badge` - Badge text displayed at the end of the `flux:label` component when the `label` prop is provided.
- `disabled` - Prevents user interaction with the datetime picker.
- `invalid` - Applies error styling to the datetime picker. Applied automatically when the bound property has a validation error.

**Slot:**

- `trigger` - Custom trigger to open the picker, such as a `flux:button`.

**Event:**

- `open` - Dispatched when the picker opens.
- `close` - Dispatched when the picker closes.
- `clear` - Dispatched when the selection is cleared using the clear button.

**Attribute:**

- `data-flux-datetime-picker` - Applied to the root element for styling and identification.
- `data-open` - Applied to the root element while the picker is open.

### flux:datetime-picker.button

**Prop:**

- `placeholder` - Text displayed when nothing is selected.
- `size` - Size of the button. Options: `sm`, `xs`.
- `clearable` - Displays a clear button when a datetime is selected.
- `invalid` - Applies error styling to the button.

### DateTimeRange Object

A specialized object for datetime ranges when using `mode="range"`.

**Method:**

- `$range->start()` - Get the start datetime as a Carbon instance.
- `$range->end()` - Get the end datetime as a Carbon instance.
- `$range->hasStart()` - Check if the range has a start datetime.
- `$range->hasEnd()` - Check if the range has an end datetime.
