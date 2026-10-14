<!-- Adding a plugin? See CONTRIBUTING.md. Title: "Add <Plugin name>". -->

**Plugin:** <!-- name and https://github.com/owner/repo -->

**What it does:** <!-- one or two sentences -->

**On the user's PC it:** <!-- programs it runs, files it writes, network, what it sends to an AI, typing into agent cards; "nothing else" if so -->

### Checklist

- [ ] The repository is public, with `plugin.json`, a README, a LICENSE and `preview.png` at its top
- [ ] The README says what the plugin does on the user's PC (programs, files, network, AI, agent cards)
- [ ] `super-desktop plugin check <id>` prints OK (no errors, no warnings)
- [ ] `super-desktop plugin publish <id>` says it is ready
- [ ] It installs on a clean setup: `super-desktop plugin install https://github.com/<owner>/<repo>`
- [ ] The entry is in id order, and `id`, `name`, `api`, `minHost` and `slots` match `plugin.json`
- [ ] `python3 validate.py` passes
- [ ] The id is new (a changed copy of a listed plugin has its own id)
