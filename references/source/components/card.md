# Card

A container for related content, such as a form, a list, or a summary. Give it a header, a body, and a footer, and the card handles the spacing, dividers, and corners between them.

```blade
<flux:card body="inset" variant="soft" size="lg">
    <flux:card.header>
        <flux:card.heading>Profile</flux:card.heading>
        <flux:card.subheading>This is how others will see you</flux:card.subheading>

        <flux:card.actions>
            <flux:button size="sm" variant="ghost" icon="ellipsis-horizontal" aria-label="More options" />
        </flux:card.actions>
    </flux:card.header>

    <flux:card.body class="space-y-6">
        <flux:input label="Name" value="Olivia Martin" />
        <flux:textarea label="Bio" rows="2" placeholder="A few words about yourself" />
    </flux:card.body>

    <flux:card.footer>
        <flux:text>Last saved 2 minutes ago</flux:text>

        <flux:card.actions>
            <flux:button variant="ghost">Cancel</flux:button>
            <flux:button variant="primary">Save</flux:button>
        </flux:card.actions>
    </flux:card.footer>
</flux:card>
```

## Simple card

Parts are optional. Put anything straight inside a card and it's padded evenly, like a div with a border.

```blade
<flux:card>
    <flux:heading size="lg">Are you sure?</flux:heading>

    <flux:text class="mt-2 mb-4">
        Your post will be deleted permanently.<br>
        This action cannot be undone.
    </flux:text>

    <flux:button variant="danger">Delete</flux:button>
</flux:card>
```

## Variants

Use the `variant` prop to change the card's surface. The default surface has a shadow in light mode and elevation in dark mode. The outline surface has neither. Tinted variants adapt to the color behind them.

```blade
<flux:card>
    <flux:heading>default</flux:heading>
    <flux:text class="mt-1">Raised, for primary content.</flux:text>
</flux:card>

<flux:card variant="muted">...</flux:card>
<flux:card variant="soft">...</flux:card>
<flux:card variant="outline">...</flux:card>
<flux:card variant="filled">...</flux:card>
```

## Sizes

Use the `size` prop to scale the card's padding, corners, and the space between its parts. Cards are `md` by default.

```blade
<flux:card size="xs" body="separated">
    <flux:card.header>
        <flux:card.heading>xs</flux:card.heading>

        <flux:card.actions>
            <flux:button size="sm">Edit</flux:button>
        </flux:card.actions>
    </flux:card.header>

    <flux:card.body>
        <flux:text>Compact, for dense lists and sidebars.</flux:text>
    </flux:card.body>
</flux:card>

<flux:card size="sm" body="separated">...</flux:card>
<flux:card size="md" body="separated">...</flux:card>
<flux:card size="lg" body="separated">...</flux:card>
```

## Body treatments

Wrap a card's main content in `flux:card.body`, optionally with a `flux:card.header` above it and a `flux:card.footer` below. The `body` prop decides how they're set apart. Buttons in `flux:card.actions` line up with the edge for you.

### Seamless

The default. Everything shares one surface, separated only by space.

```blade
<flux:card body="seamless">
    <flux:card.header>
        <flux:card.heading>Notifications</flux:card.heading>
        <flux:card.subheading>Choose what you hear about</flux:card.subheading>
    </flux:card.header>

    <flux:card.body class="space-y-4">
        <flux:switch label="Product updates" checked />
        <flux:switch label="Weekly digest" />
        <flux:switch label="Security alerts" checked />
    </flux:card.body>
</flux:card>
```

### Inset

Set the body in its own panel, a little in from the card's edges. On a tinted card the panel is raised; on a white one it's a recessed well.

```blade
<flux:card body="inset" variant="soft">
    ...
</flux:card>
```

### Flush

Like inset, but the panel runs all the way to the card's sides.

```blade
<flux:card body="flush" variant="soft">
    ...
</flux:card>
```

### Divided

Separate the header and footer from the body with lines. Add `divider="inset"` to stop the lines at the content's edges instead of running them across the card.

```blade
<flux:card body="divided">
    ...
</flux:card>

<flux:card body="divided" divider="inset">
    ...
</flux:card>
```

### Separated

Set the header and footer apart as tinted bands around the body.

```blade
<flux:card body="separated">
    ...
</flux:card>
```

## Bleed

Run content out to the card's edges, so it reaches the nearest visible edge instead of sitting inside the padding.

### Images

Wrap media in `flux:card.bleed`. It always reaches the sides, reaches the top or bottom when it's the first or last thing in the body, and rounds only the corners it touches.

```blade
<flux:card body="inset">
    <flux:card.body>
        <flux:card.bleed>
            <img src="/img/forest.png" alt="A misty forest path" class="block aspect-video w-full object-cover">
        </flux:card.bleed>
    </flux:card.body>

    <flux:card.footer>
        <flux:card.heading>Morning hike</flux:card.heading>
        <flux:card.subheading>Sept 12</flux:card.subheading>

        <flux:card.actions>
            <flux:button size="sm" variant="ghost" icon="ellipsis-horizontal" aria-label="More options" />
        </flux:card.actions>
    </flux:card.footer>
</flux:card>
```

### Tables

A [table](https://fluxui.dev/components/table) with the `bleed` prop bleeds the same way: its rows run edge to edge while their content lines up with the card's, and as the only thing in the body it reaches the body's top and bottom.

```blade
<flux:card variant="muted" body="flush">
    <flux:card.header>
        <flux:card.heading>Past transactions</flux:card.heading>

        <flux:card.actions>
            <flux:button size="sm" variant="filled" icon="adjustments-horizontal" aria-label="Filter transactions" />
        </flux:card.actions>
    </flux:card.header>

    <flux:card.body>
        <flux:table bleed>
            <flux:table.rows>
                <flux:table.row>
                    <flux:table.cell>
                        <flux:heading>Blue Bottle Coffee</flux:heading>
                        <flux:text class="text-xs">Dining</flux:text>
                    </flux:table.cell>

                    <flux:table.cell align="end" class="font-medium tabular-nums">−$6.75</flux:table.cell>
                </flux:table.row>

                <!-- ... -->
            </flux:table.rows>
        </flux:table>
    </flux:card.body>
</flux:card>
```

## Outside a card

Headers and footers work on their own too, like a section heading above a card. Set their `size` to match the card beside them.

```blade
<flux:card.header>
    <flux:card.heading size="lg">Security</flux:card.heading>

    <flux:card.actions>
        <flux:button size="sm" variant="outline">Activity log</flux:button>
    </flux:card.actions>
</flux:card.header>

<flux:card>
    <div class="flex items-center justify-between gap-4">
        <div>
            <flux:heading>Password</flux:heading>
            <flux:text class="mt-1">Last changed 3 months ago</flux:text>
        </div>

        <flux:button size="sm">Change</flux:button>
    </div>

    <flux:separator variant="subtle" class="my-4" />

    <div class="flex items-center justify-between gap-4">
        <div>
            <flux:heading>Two-factor authentication</flux:heading>
            <flux:text class="mt-1">A code from your authenticator app</flux:text>
        </div>

        <flux:badge size="sm" color="green">On</flux:badge>
    </div>
</flux:card>
```

## Inside a body

Inside a body, a header or footer becomes a sub-section of it, bare whatever the card's body treatment. Use them to break a body into titled groups.

```blade
<flux:card body="inset" variant="soft">
    <flux:card.header>
        <flux:card.heading>Billing</flux:card.heading>
        <flux:card.subheading>Manage your plan and payments</flux:card.subheading>
    </flux:card.header>

    <flux:card.body>
        <flux:card.header>
            <flux:card.heading>Pro plan</flux:card.heading>
            <flux:card.subheading>$24 per month, renews Oct 12</flux:card.subheading>

            <flux:card.actions>
                <flux:button size="sm">Change plan</flux:button>
            </flux:card.actions>
        </flux:card.header>

        <div class="space-y-2">
            <div class="flex justify-between">
                <flux:text>Seats used</flux:text>
                <flux:text variant="strong">8 of 10</flux:text>
            </div>

            <flux:progress value="80" />
        </div>

        <flux:separator variant="subtle" class="my-6" />

        <flux:card.header>
            <flux:card.heading>Payment method</flux:card.heading>

            <flux:card.actions>
                <flux:button size="sm" variant="ghost">Update</flux:button>
            </flux:card.actions>
        </flux:card.header>

        <div class="flex items-center gap-3">
            <flux:icon.credit-card variant="outline" class="text-zinc-400" />
            <flux:text>Visa ending in 4242 · Expires 08/28</flux:text>
        </div>
    </flux:card.body>

    <flux:card.footer>
        <flux:text>Invoices are emailed to billing@acme.com</flux:text>
    </flux:card.footer>
</flux:card>
```

## Link card

Wrap a small card in a link for compact, clickable content like announcements or shortcuts.

```blade
<a href="#" aria-label="Latest on our blog">
    <flux:card size="xs" class="hover:bg-zinc-50 dark:hover:bg-zinc-700">
        <flux:heading class="flex items-center gap-2">Latest on our blog <flux:icon name="arrow-up-right" class="ml-auto text-zinc-400" variant="micro" /></flux:heading>
        <flux:text class="mt-2">Stay up to date with our latest insights, tutorials, and product updates.</flux:text>
    </flux:card>
</a>
```

## Related

- [Heading](https://fluxui.dev/components/heading) - Create hierarchical section headings for content
- [Table](https://fluxui.dev/components/table) - Display structured data, with rows that bleed to a card's edges

## Reference

### flux:card

**Prop:**

- `body` - How the header, body, and footer are set apart. Options: `seamless` (default), `inset`, `flush`, `divided`, `separated`.
- `variant` - Visual treatment of the card's surface. Options: `muted`, `soft`, `outline`, `filled`. Default: `default`, with a shadow in light mode and elevation in dark mode. `outline` keeps the border without the shadow or dark-mode elevation.
- `size` - Scales the card's padding, corners, and spacing. Options: `xs`, `sm`, `md` (default), `lg`.
- `divider` - With `body="divided"`, set to `inset` to stop the dividers at the content's edges.
- `highlight` - A faint highlight along the inside of the card's top edge, in light mode. Default: `true`. Pass `:highlight="false"` to turn it off.

**Slot:**

- `default` - The card's parts, or any content to pad evenly.

**Attribute:**

- `data-flux-card` - Applied to the root element for styling and identification.

### flux:card.header

**Prop:**

- `size` - When used outside a card, matches the size of the card it sits beside. Inside a card, the card's size applies.

**Slot:**

- `default` - A `flux:card.heading`, an optional `flux:card.subheading`, and optional `flux:card.actions`.

### flux:card.heading

**Prop:**

- `size` - Options: `base` (default), `lg`, `xl`.
- `level` - The heading level to render, such as `2` for an `h2`.

### flux:card.subheading

**Slot:**

- `default` - Supporting text, tucked under the heading before it.

### flux:card.actions

**Slot:**

- `default` - Buttons or other controls. In a header they center on the heading and tuck into the corner rather than making the header taller. Placed after the heading they sit at the end; placed before it, at the start.

### flux:card.body

**Slot:**

- `default` - The card's main content. Can also hold its own header and footer, which then act as a sub-section.

### flux:card.footer

**Prop:**

- `size` - When used outside a card, matches the size of the card it sits beside.

**Slot:**

- `default` - Supporting text and optional `flux:card.actions`.

### flux:card.bleed

**Slot:**

- `default` - Media to run out to the card's edges, such as an image.

**CSS Variable:**

- `--flux-bleed-x` - How far content reaches sideways to the nearest visible edge. Also available as `--flux-bleed`. Set automatically by cards.
- `--flux-bleed-top / --flux-bleed-bottom` - How far content at the start or end of a body reaches up or down.
- `--flux-bleed-top-radius / --flux-bleed-bottom-radius` - The radius of the corners that bleeding content reaches.
