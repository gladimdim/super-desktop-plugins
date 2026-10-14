# SUPER DESKTOP plugins

The public list of plugins for [SUPER DESKTOP](https://github.com/gladimdim/super-desktop).
Each plugin lives in its own git repository; `registry.json` lists them so
people, and SUPER DESKTOP itself, can find them.

| Plugin | What it does | Needs |
| --- | --- | --- |
| [Reminder](https://github.com/gladimdim/super-desktop-reminder) | A bell in the top bar: click it to add a reminder, right-click it to see and remove them. When one is due it notifies, plays a ding-dong and the bell shakes. | 1.6.0 |

Listing is not a review. Read a plugin's README before you install it:
plugins run as you.

## Install a plugin

```sh
super-desktop plugin install https://github.com/<owner>/<plugin-repo>
super-desktop plugin approve <plugin id>
```

An installed plugin runs only once you approve it, here or in Settings →
Plugins, where **Ask AI to review** reads it first.
`super-desktop plugin update <plugin id>` brings it up to date.

## For SUPER DESKTOP and other tools

The list is at
`https://raw.githubusercontent.com/gladimdim/super-desktop-plugins/main/registry.json`,
described by `registry.schema.json` (`registryVersion` 2). A plugin installs
from `https://github.com/<repo>`; `api` and `minHost` say whether this SUPER
DESKTOP can run it, `slots` where it appears.

## Add your plugin

1. Build it with SUPER DESKTOP's plugin skill (✨ Create Plugin, or
   `super-desktop plugin new <id>`), keep `plugin.json` at the top of its
   repository, and make `super-desktop plugin check <id>` pass with no errors
   or warnings. A README that says what it does on the user's PC (programs it
   runs, files it writes, anything it sends) helps it get listed.
2. Open a pull request that adds an entry to `registry.json`, in id order:

   ```json
   {
     "id": "your-id",
     "name": "Your Plugin",
     "description": "One or two sentences of what the user gets.",
     "repo": "you/your-plugin-repo",
     "tags": ["productivity"],
     "author": "you",
     "api": 1,
     "minHost": "1.6.0",
     "slots": ["popup", "toolbar.item"]
   }
   ```

   `id`, `name` and `api` must match your `plugin.json`, and `slots` (sorted)
   its surfaces' slots. `minHost` is the lowest SUPER DESKTOP version with
   everything it uses.
3. `python3 validate.py` (needs `pip install jsonschema`) runs the same checks
   as CI, including reading your `plugin.json` from GitHub.
