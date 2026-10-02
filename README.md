# SUPER DESKTOP plugins

The registry of plugins for [SUPER DESKTOP](https://github.com/gladimdim/super-desktop).
Each plugin lives in its own repository; `registry.json` lists them so people
can find them.

| Plugin | What it does |
| --- | --- |
| [Flusher](https://github.com/gladimdim/super-desktop-flusher) | Lists the git repositories in your folders that have uncommitted changes; Flush starts an agent that commits them meaningfully and pushes each current branch. |
| [Gravity WM](https://github.com/gladimdim/super-desktop-gravity-wm) | Cards grow toward the horizontal centre, up to 70% of the screen width with more rows and columns, shrink toward the sides and become icons at the edges. |

Listing is not a review. Read a plugin's README and permissions before you
install it: plugins run as you.

## Install a plugin

```sh
git clone https://github.com/<owner>/<plugin-repo>
super-desktop plugin link <plugin-repo>
super-desktop plugin activate <plugin id>
```

## Add your plugin

1. Write it with the `super-desktop-plugin` skill
   (`super-desktop plugin new <id>` starts one), make
   `super-desktop plugin validate .` and `super-desktop plugin test .` pass,
   and release a `v<version>` tag.
2. Open a pull request that adds an entry to `registry.json`, in id order:

   ```json
   {
     "id": "your-id",
     "name": "Your Plugin",
     "description": "One sentence of what the user gets.",
     "repo": "you/your-plugin-repo",
     "tags": ["git"],
     "author": "you",
     "minHost": "1.2.0"
   }
   ```

   `id` and `name` must match your manifest, and `minHost` the lower bound of
   its `engines.superDesktop`. `registry.schema.json` describes the file.
3. `python3 validate.py` (needs `pip install jsonschema`) runs the same
   checks as CI.

`reviewedTag` and `reviewedCommit` mark a version reviewed with the
`super-desktop-plugin-review` skill by someone other than its author.
