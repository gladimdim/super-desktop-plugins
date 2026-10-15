# SUPER DESKTOP plugins

The public list of plugins for [SUPER DESKTOP](https://github.com/gladimdim/super-desktop).
Each plugin lives in its own git repository; `registry.json` lists them so
people, and SUPER DESKTOP itself, can find them.

| Plugin | What it does | Needs |
| --- | --- | --- |
| [Agents button](https://github.com/gladimdim/super-desktop-harness-single-button) | One top-bar button that opens a list of the agents turned on in Settings, each with its icon and name; click one to open a new card for it. | 1.5.0 |
| [Focus timer](https://github.com/gladimdim/super-desktop-focus-timer) | A countdown timer in the top bar: click to start one (5, 15, 25 min or your own, with a label), right-click for finished timers. When one ends it notifies, plays an alarm and flashes. | 1.6.0 |
| [Reminder](https://github.com/gladimdim/super-desktop-reminder) | A bell in the top bar: click it to add a reminder, right-click it to see and remove them. When one is due it notifies, plays a ding-dong and the bell shakes. | 1.6.0 |
| [TicTacToe](https://github.com/gladimdim/super-desktop-tictactoe) | A tic-tac-toe game that stays on the desktop: a big board with the score beside it, against the computer or a friend. A # in the top bar brings the panel back. | 1.6.0 |

Listing is not a review. Read a plugin's README before you install it:
plugins run as you.

## Install a plugin

In SUPER DESKTOP: **Settings → Plugins → Discover** shows this list
(search, a category, grouped by category) with **Install**, and **Edit &
Enhance**, which makes a plugin your own copy and opens an AI agent to
improve it. In a
terminal:

```sh
super-desktop plugin search [text]          # this list, by category
super-desktop plugin install <plugin id>    # from its repository, checked against this list
super-desktop plugin approve <plugin id>
```

`super-desktop plugin install https://github.com/<owner>/<repo>` installs a
plugin that is not listed.

An installed plugin runs only once you approve it, here or in Settings →
Plugins, where **Ask AI to review** reads it first.
`super-desktop plugin update <plugin id>` brings it up to date.

## For SUPER DESKTOP and other tools

SUPER DESKTOP reads this list (Discover, `plugin search`, `plugin install
<id>`); it refuses an entry whose repository's `plugin.json` has another id,
and leaves out entries that are not well formed. The list is at
`https://raw.githubusercontent.com/gladimdim/super-desktop-plugins/main/registry.json`,
described by `registry.schema.json` (`registryVersion` 2). A plugin installs
from `https://github.com/<repo>`; `api` and `minHost` say whether this SUPER
DESKTOP can run it, `slots` where it appears.

## Add your plugin

Your plugin stays in your own public GitHub repository; a pull request adds
one entry for it to `registry.json`. In short:

1. Make it with SUPER DESKTOP's plugin skill (✨ Create Plugin, or
   `super-desktop plugin new <id>`), with `plugin.json`, a README that says
   what it does on the user's PC, a LICENSE and a `preview.png` at the top.
2. `super-desktop plugin check <id>` must pass; `super-desktop plugin publish
   <id>` checks the rest and prints your entry.
3. [Edit registry.json](https://github.com/gladimdim/super-desktop-plugins/edit/main/registry.json)
   on GitHub (it forks for you), add the entry in id order, and open the pull
   request. `python3 validate.py` runs the same checks as CI.

**[CONTRIBUTING.md](CONTRIBUTING.md)** has every step: the fields, the
preview, checking it installs, the git and `gh` commands, what reviewers
look at, and how to update or remove an entry.
