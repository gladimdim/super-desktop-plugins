# Add your plugin to the list

This repository is the public list of [SUPER DESKTOP](https://github.com/gladimdim/super-desktop)
plugins. Your plugin stays in **your own repository**; you add one entry for
it to `registry.json` with a pull request. Once it is merged, everyone sees
it in **Settings → Plugins → Discover** and in `super-desktop plugin search`.

Listing is not a review of every line, and installing never runs a plugin
until its user approves it. We still read what you send, so make it easy to
see what your plugin does.

## 1. Make the plugin

The easiest way is to let an AI agent build it with SUPER DESKTOP's plugin
skill:

- **✨ Create Plugin** in SUPER DESKTOP's top bar (or Settings → Plugins), or
- `super-desktop plugin new <id> --slot toolbar.item`, then open an agent in
  `~/.config/super-desktop/plugins/<id>/`: it reads `AGENTS.md` and
  `.claude/skills/super-desktop-plugin/SKILL.md`.

To start from a plugin in this list, use **Edit & Enhance** on it (or
`super-desktop plugin fork <id>`), then give your copy a **new id** before you
publish it (rename the folder and change `"id"` in `plugin.json`). Two
entries cannot share an id.

## 2. Make it ready

Your repository must be **public on GitHub** with `plugin.json` at its top
level (the plugin folder is the repository).

**plugin.json**

```json
{
  "id": "weather-dock",
  "name": "Weather dock",
  "description": "Today's weather on the right edge; click for the week.",
  "version": "1.0.0",
  "minHost": "1.6.0",
  "categories": ["weather"],
  "api": 1,
  "surfaces": [ ... ]
}
```

- `id`: lowercase letters, digits and `-`, unique in this list. Do not reuse
  someone else's id or a name that looks like another project's.
- `version`: raise it with every release.
- `minHost`: the oldest SUPER DESKTOP that has everything your plugin uses,
  i.e. the version you tested with.
- `categories` (up to 5): Discover groups plugins by them. Reuse one that
  exists if it fits: `productivity`, `time`, `games`, `agents`, `system`,
  `weather`, `fun`…

**README.md** that says, in plain words:

- what it does and how to use it (where it appears, what a click does);
- what it does **on the user's PC**: programs it runs (`sd.run`,
  `sd.exec`), files it reads or writes, network requests, what it sends to
  an AI (`llm.complete`), whether it types into agent cards (`cards.send`);
- the license (add a `LICENSE` file; MIT is common).

**preview.png** at the top of the repository: 1280×640, at most 1.5 MiB, the
plugin in use with sample data. Discover shows its middle square, so keep
the important part in the middle.

```sh
super-desktop plugin preview <id> --values sample.json   # draws preview.png (SUPER DESKTOP 1.6.0+)
```

**Do not commit** `.claude/` (SUPER DESKTOP adds its skill itself), secrets,
build output or large files. Add `.claude/` to `.gitignore`.

## 3. Check it

```sh
super-desktop plugin check <id>        # must print OK: no errors, no warnings
super-desktop plugin snapshot <id> --surface <surface> --out /tmp/shot.png
super-desktop plugin publish <id>      # readiness, then the entry to add
```

`plugin preview` and `plugin publish` come with SUPER DESKTOP 1.6.0.
`plugin publish` changes nothing. It checks what this list needs (a clean
check, `minHost`, a description, a README, the repository on GitHub with
everything committed and pushed, no `.claude/` in git) and prints your entry
for `registry.json`.

Also check that it installs on a clean setup:

```sh
SD_PLUGINS_DIR=/tmp/try/plugins SD_PLUGINS_STATE_DIR=/tmp/try/state \
  super-desktop plugin install https://github.com/<you>/<repo>
```

## 4. Open the pull request

Add your entry to the `"plugins"` array in `registry.json`, **in id order**:

```json
{
  "id": "weather-dock",
  "name": "Weather dock",
  "description": "Today's weather on the right edge; click for the week.",
  "repo": "you/super-desktop-weather-dock",
  "tags": ["weather"],
  "author": "you",
  "api": 1,
  "minHost": "1.6.0",
  "slots": ["dock.right", "popup"]
}
```

| Field | Rule |
| --- | --- |
| `id`, `name`, `api` | Exactly as in your `plugin.json`. |
| `description` | At most 200 characters: what the user gets. |
| `repo` | `owner/name` of the GitHub repository. |
| `tags` | Your `plugin.json` `categories`. |
| `author` | Your GitHub name (or your name). |
| `minHost` | As in your `plugin.json`, three numbers (`1.6.0`). |
| `slots` | Every `slot` of your surfaces, sorted, no repeats. |

### In the browser (no tools needed)

1. Open [registry.json → Edit](https://github.com/gladimdim/super-desktop-plugins/edit/main/registry.json).
   GitHub makes a fork for you.
2. Paste your entry in id order. Mind the commas between entries.
3. **Propose changes**, then **Create pull request**. Title: `Add <Name>`.
4. Fill in the checklist that appears.

### With git and the GitHub CLI

```sh
gh repo fork gladimdim/super-desktop-plugins --clone
cd super-desktop-plugins
git switch -c add-weather-dock
$EDITOR registry.json                  # add the entry, in id order
pip install jsonschema && python3 validate.py
git commit -am "Add Weather dock"
git push -u origin add-weather-dock
gh pr create --fill
```

`python3 validate.py` runs the same checks as CI: the schema, ids unique and
in order, sorted slots, and your `plugin.json` read from GitHub (same `id`,
`name`, `api` and slots). A missing `preview.png` is only a note.
`python3 validate.py --offline` skips GitHub.

## 5. Review

CI runs `validate.py` on every pull request; it must pass. A maintainer then:

- reads the plugin's QML and JavaScript, looking for what the README should
  have said: programs it runs, files, network, data sent anywhere, typing
  into agents, anything obfuscated or downloaded at run time;
- installs it, approves it and tries it;
- checks the description, the preview and the id.

We may ask for changes. We do not list plugins that hide what they do,
collect data without saying so, impersonate others, or need a SUPER
DESKTOP that is not released yet.

Once merged, SUPER DESKTOP shows it after its next fetch of the list
(Discover's ↻ fetches it at once).

## Update or remove your entry

- **A new release of your plugin** needs no pull request: users get it with
  `super-desktop plugin update <id>`. Raise `version` in `plugin.json`.
- **Change the entry** (description, tags, `minHost`, a renamed repository):
  a pull request that edits it, with the reason.
- **Remove it**: a pull request that deletes the entry, or open an issue.

Questions: open an issue in this repository.
