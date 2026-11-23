# Item

A row with a heading, a line of supporting text, and a control at the end. Group items together for settings pages, account details, and lists of people or connections.

```blade
<flux:item>
    <flux:item.media>
        <flux:avatar circle src="https://unavatar.io/x/calebporzio" />
    </flux:item.media>

    <flux:item.heading>Caleb Porzio</flux:item.heading>
    <flux:item.subheading>caleb@example.com</flux:item.subheading>

    <flux:item.actions>
        <flux:button size="sm" icon:trailing="arrow-up-right">Edit profile</flux:button>
    </flux:item.actions>
</flux:item>

<flux:item.group>
    <flux:item>
        <flux:item.heading>Two-factor authentication</flux:item.heading>
        <flux:item.subheading>Ask for a code when you sign in on a new device.</flux:item.subheading>

        <flux:item.actions>
            <flux:switch aria-label="Two-factor authentication" checked />
        </flux:item.actions>
    </flux:item>

    <flux:item>
        <flux:item.heading>Language</flux:item.heading>

        <flux:item.actions>
            <flux:dropdown align="end">
                <flux:button size="sm" variant="ghost" icon:trailing="chevron-down" inset="right">English</flux:button>

                <flux:menu>
                    <flux:menu.radio.group>
                        <flux:menu.radio checked>English</flux:menu.radio>
                        <flux:menu.radio>Español</flux:menu.radio>
                        <flux:menu.radio>Français</flux:menu.radio>
                    </flux:menu.radio.group>
                </flux:menu>
            </flux:dropdown>
        </flux:item.actions>
    </flux:item>

    <flux:item>
        <flux:item.heading>Sign out everywhere else</flux:item.heading>
        <flux:item.subheading>You're signed in on 3 other devices.</flux:item.subheading>

        <flux:item.actions>
            <flux:button size="sm">Sign out</flux:button>
        </flux:item.actions>
    </flux:item>
</flux:item.group>
```

## Single item

A single item doesn't need a group. On its own, it draws the same surface a group would.

```blade
<flux:item>
    <flux:item.heading>Sign out</flux:item.heading>
    <flux:item.subheading>Your boards stay on this device.</flux:item.subheading>

    <flux:item.actions>
        <flux:button size="sm">Sign out</flux:button>
    </flux:item.actions>
</flux:item>
```

## Without a subheading

The subheading is optional. Without one, an item is a single line, still as tall as a small button so rows stay even.

```blade
<flux:item.group>
    <flux:item>
        <flux:item.heading>Subscribed since</flux:item.heading>

        <flux:item.actions>
            <flux:text>October 4, 2026</flux:text>
        </flux:item.actions>
    </flux:item>

    <flux:item>
        <flux:item.heading>Seats</flux:item.heading>

        <flux:item.actions>
            <flux:text>3 of 5 used</flux:text>
        </flux:item.actions>
    </flux:item>

    <flux:item>
        <flux:item.heading>Renew automatically</flux:item.heading>

        <flux:item.actions>
            <flux:switch aria-label="Renew automatically" checked />
        </flux:item.actions>
    </flux:item>
</flux:item.group>
```

## Actions

Put buttons, a switch, or a value in `flux:item.actions`. It sits at the end of the row, centered on the heading and subheading beside it. Several things sit side by side.

```blade
<flux:item.group>
    <flux:item>
        <flux:item.heading>Claude Code</flux:item.heading>
        <flux:item.subheading>Not found on this computer.</flux:item.subheading>

        <flux:item.actions>
            <flux:button size="sm" variant="subtle">Browse…</flux:button>
            <flux:button size="sm">Install</flux:button>
        </flux:item.actions>
    </flux:item>

    <flux:item>
        <flux:item.heading>Send error reports</flux:item.heading>
        <flux:item.subheading>When something goes wrong, we get a report so it can be fixed.</flux:item.subheading>

        <flux:item.actions>
            <flux:switch aria-label="Send error reports" checked />
        </flux:item.actions>
    </flux:item>

    <flux:item>
        <flux:item.heading>Next payment</flux:item.heading>
        <flux:item.subheading>December 4, 2026</flux:item.subheading>

        <flux:item.actions>
            <flux:heading>$60.00</flux:heading>
        </flux:item.actions>
    </flux:item>
</flux:item.group>
```

## Media

Put an avatar, an icon, or anything else that leads the row in `flux:item.media`. It sits at the start, centered on the text beside it.

```blade
<flux:item.group>
    <flux:item>
        <flux:item.media>
            <flux:avatar size="sm" circle src="https://unavatar.io/x/calebporzio" />
        </flux:item.media>

        <flux:item.heading>Caleb Porzio</flux:item.heading>
        <flux:item.subheading>caleb@example.com</flux:item.subheading>
    </flux:item>

    <flux:item>
        <flux:item.media>
            <flux:avatar size="sm" icon="command-line" />
        </flux:item.media>

        <flux:item.heading>Claude Code</flux:item.heading>
        <flux:item.subheading>Version 2.1.4</flux:item.subheading>
    </flux:item>

    <flux:item>
        <flux:item.media>
            <flux:avatar size="sm" initials="N" />
        </flux:item.media>

        <flux:item.heading>Northwind</flux:item.heading>
        <flux:item.subheading>8 boards</flux:item.subheading>
    </flux:item>
</flux:item.group>
```

## Narrow widths

On a narrow item, like one on a phone, a labeled button moves under the text so the heading keeps its room. Switches, values, menus, and icon buttons stay at the end of the row. The item goes by its own width rather than the screen's, so it does the same in a modal or a sidebar.

```blade
<flux:item>
    <flux:item.media>
        <flux:avatar circle src="https://unavatar.io/x/calebporzio" />
    </flux:item.media>

    <flux:item.heading>Caleb Porzio</flux:item.heading>
    <flux:item.subheading>caleb@example.com</flux:item.subheading>

    <flux:item.actions>
        <flux:button size="sm" icon:trailing="arrow-up-right">Edit profile</flux:button>
    </flux:item.actions>
</flux:item>

<flux:item.group>
    <flux:item>
        <flux:item.heading>Claude Code</flux:item.heading>
        <flux:item.subheading>Not found on this computer.</flux:item.subheading>

        <flux:item.actions>
            <flux:button size="sm" variant="subtle">Browse…</flux:button>
            <flux:button size="sm">Install</flux:button>
        </flux:item.actions>
    </flux:item>

    <flux:item>
        <flux:item.heading>Send error reports</flux:item.heading>
        <flux:item.subheading>When something goes wrong, we get a report so it can be fixed.</flux:item.subheading>

        <flux:item.actions>
            <flux:switch aria-label="Send error reports" checked />
        </flux:item.actions>
    </flux:item>
</flux:item.group>
```

## Examples

### Team members

People on a team, each with their role. Roles you can change open a menu.

```blade
<flux:item.group>
    <flux:item>
        <flux:item.media>
            <flux:avatar size="sm" circle src="https://unavatar.io/x/calebporzio" />
        </flux:item.media>

        <flux:item.heading>Caleb Porzio <flux:text inline variant="subtle">(you)</flux:text></flux:item.heading>
        <flux:item.subheading>caleb@example.com</flux:item.subheading>

        <flux:item.actions>
            <flux:text>Owner</flux:text>
        </flux:item.actions>
    </flux:item>

    <flux:item>
        <flux:item.media>
            <flux:avatar size="sm" circle src="https://unavatar.io/github/joshhanley" />
        </flux:item.media>

        <flux:item.heading>Josh Hanley</flux:item.heading>
        <flux:item.subheading>josh@example.com</flux:item.subheading>

        <flux:item.actions>
            <flux:dropdown align="end">
                <flux:button size="sm" variant="ghost" icon:trailing="chevron-down" inset="right">Admin</flux:button>

                <flux:menu>
                    <flux:menu.radio.group>
                        <flux:menu.radio checked>Admin</flux:menu.radio>
                        <flux:menu.radio>Member</flux:menu.radio>
                    </flux:menu.radio.group>

                    <flux:menu.separator />

                    <flux:menu.item variant="danger">Remove from team…</flux:menu.item>
                </flux:menu>
            </flux:dropdown>
        </flux:item.actions>
    </flux:item>

    <flux:item>
        <flux:item.media>
            <flux:avatar size="sm" circle src="https://unavatar.io/github/hugosaintemarie" />
        </flux:item.media>

        <flux:item.heading>Hugo Sainte-Marie</flux:item.heading>
        <flux:item.subheading>hugo@example.com</flux:item.subheading>

        <flux:item.actions>
            <flux:dropdown align="end">
                <flux:button size="sm" variant="ghost" icon:trailing="chevron-down" inset="right">Member</flux:button>

                <flux:menu>
                    <flux:menu.radio.group>
                        <flux:menu.radio>Admin</flux:menu.radio>
                        <flux:menu.radio checked>Member</flux:menu.radio>
                    </flux:menu.radio.group>

                    <flux:menu.separator />

                    <flux:menu.item variant="danger">Remove from team…</flux:menu.item>
                </flux:menu>
            </flux:dropdown>
        </flux:item.actions>
    </flux:item>

    <flux:item>
        <flux:item.media>
            <flux:avatar size="sm" circle icon="envelope" />
        </flux:item.media>

        <flux:item.heading>mia@example.com</flux:item.heading>
        <flux:item.subheading>Invited 2 days ago</flux:item.subheading>

        <flux:item.actions>
            <flux:dropdown align="end">
                <flux:button size="sm" variant="ghost" icon="ellipsis-horizontal" aria-label="Invite options" />

                <flux:menu>
                    <flux:menu.item>Resend invite</flux:menu.item>
                    <flux:menu.item variant="danger">Revoke invite</flux:menu.item>
                </flux:menu>
            </flux:dropdown>
        </flux:item.actions>
    </flux:item>
</flux:item.group>
```

### Connected apps

Apps with access to an account, when each was last used, and a menu to disconnect it.

```blade
<flux:item.group>
    <flux:item>
        <flux:item.heading>Grok Bot</flux:item.heading>

        <flux:item.actions>
            <flux:text>Used 4 minutes ago</flux:text>

            <flux:dropdown align="end">
                <flux:button size="sm" variant="ghost" icon="ellipsis-horizontal" aria-label="Grok Bot options" />

                <flux:menu>
                    <flux:menu.item variant="danger">Disconnect…</flux:menu.item>
                </flux:menu>
            </flux:dropdown>
        </flux:item.actions>
    </flux:item>

    <flux:item>
        <flux:item.heading>Amp</flux:item.heading>

        <flux:item.actions>
            <flux:text>Used yesterday</flux:text>

            <flux:dropdown align="end">
                <flux:button size="sm" variant="ghost" icon="ellipsis-horizontal" aria-label="Amp options" />

                <flux:menu>
                    <flux:menu.item variant="danger">Disconnect…</flux:menu.item>
                </flux:menu>
            </flux:dropdown>
        </flux:item.actions>
    </flux:item>

    <flux:item>
        <flux:item.heading>Cursor</flux:item.heading>

        <flux:item.actions>
            <flux:text>Never used</flux:text>

            <flux:dropdown align="end">
                <flux:button size="sm" variant="ghost" icon="ellipsis-horizontal" aria-label="Cursor options" />

                <flux:menu>
                    <flux:menu.item variant="danger">Disconnect…</flux:menu.item>
                </flux:menu>
            </flux:dropdown>
        </flux:item.actions>
    </flux:item>
</flux:item.group>
```

### Billing

A plan and its status, what you pay next, and a way out to manage payment details.

```blade
<flux:item.group>
    <flux:item>
        <flux:item.heading>Pro plan</flux:item.heading>
        <flux:item.subheading>$20 a month for each person</flux:item.subheading>

        <flux:item.actions>
            <flux:badge size="sm" color="green">Active</flux:badge>
        </flux:item.actions>
    </flux:item>

    <flux:item>
        <flux:item.heading>Next payment</flux:item.heading>
        <flux:item.subheading>December 4, 2026</flux:item.subheading>

        <flux:item.actions>
            <flux:heading>$60.00</flux:heading>
        </flux:item.actions>
    </flux:item>

    <flux:item>
        <flux:item.heading>Payment details and invoices</flux:item.heading>
        <flux:item.subheading>Managed by Stripe.</flux:item.subheading>

        <flux:item.actions>
            <flux:button size="sm" icon:trailing="arrow-up-right">Manage billing</flux:button>
        </flux:item.actions>
    </flux:item>
</flux:item.group>
```

### Teams

Teams you belong to, each with its mark and your role in it.

```blade
<flux:item.group>
    <flux:item>
        <flux:item.media>
            <flux:avatar size="sm" initials="P" />
        </flux:item.media>

        <flux:item.heading>Paraframe</flux:item.heading>
        <flux:item.subheading>24 boards</flux:item.subheading>

        <flux:item.actions>
            <flux:badge size="sm">Owner</flux:badge>
        </flux:item.actions>
    </flux:item>

    <flux:item>
        <flux:item.media>
            <flux:avatar size="sm" initials="N" />
        </flux:item.media>

        <flux:item.heading>Northwind</flux:item.heading>
        <flux:item.subheading>8 boards</flux:item.subheading>

        <flux:item.actions>
            <flux:badge size="sm">Member</flux:badge>
        </flux:item.actions>
    </flux:item>
</flux:item.group>
```

### Notifications

A list of preferences, each with a switch.

```blade
<flux:item.group>
    <flux:item>
        <flux:item.heading>Comments</flux:item.heading>
        <flux:item.subheading>When someone comments on a board you own.</flux:item.subheading>

        <flux:item.actions>
            <flux:switch aria-label="Comments" checked />
        </flux:item.actions>
    </flux:item>

    <flux:item>
        <flux:item.heading>Mentions</flux:item.heading>
        <flux:item.subheading>When someone mentions you anywhere.</flux:item.subheading>

        <flux:item.actions>
            <flux:switch aria-label="Mentions" checked />
        </flux:item.actions>
    </flux:item>

    <flux:item>
        <flux:item.heading>Weekly digest</flux:item.heading>
        <flux:item.subheading>A summary of what changed, every Monday.</flux:item.subheading>

        <flux:item.actions>
            <flux:switch aria-label="Weekly digest" />
        </flux:item.actions>
    </flux:item>
</flux:item.group>
```

### Danger zone

Actions that are hard to undo, kept together and apart from everything else.

```blade
<flux:item.group>
    <flux:item>
        <flux:item.heading>Transfer ownership</flux:item.heading>
        <flux:item.subheading>Give this team to someone else. You'll stay on as an admin.</flux:item.subheading>

        <flux:item.actions>
            <flux:button size="sm">Transfer…</flux:button>
        </flux:item.actions>
    </flux:item>

    <flux:item>
        <flux:item.heading>Delete team</flux:item.heading>
        <flux:item.subheading>Its boards are deleted for everyone. This can't be undone.</flux:item.subheading>

        <flux:item.actions>
            <flux:button size="sm" variant="outline" color="red">Delete…</flux:button>
        </flux:item.actions>
    </flux:item>
</flux:item.group>
```

## Reference

### flux:item.group

**Slot:**

- `default` - One or more `flux:item` components, drawn as one bordered surface with a rule between each.

### flux:item

**Slot:**

- `default` - An optional `flux:item.media`, a `flux:item.heading`, an optional `flux:item.subheading`, and optional `flux:item.actions`. Used without a group, an item draws its own surface.

### flux:item.media

**Slot:**

- `default` - An avatar, an icon, or anything else that leads the row. Sits at the start, centered on the heading and subheading. Several things sit side by side.

### flux:item.heading

**Prop:**

- `level` - The heading level to render, such as `3` for an `h3`.

### flux:item.subheading

**Slot:**

- `default` - Supporting text, tucked under the heading.

### flux:item.actions

**Slot:**

- `default` - Buttons, a switch, or a value. Sits at the end of the row, centered on the heading and subheading.
