# cmux preferred setup

Terse baseline for the cmux sidebar.

## What it does

- Each tab is named after its folder.
- The sidebar shows only the name. No branch, ports, PRs, logs or notifications.
- Tabs are sorted A to Z, ignoring case.

## Where it lives

- `~/.config/cmux/cmux.json`: sidebar settings. `sidebar.hideAllDetails` hides the extra lines.
- `~/.config/cmux/name-workspaces-by-folder.zsh`: names tabs by folder, then sorts them.
- `~/.zshrc`: runs the script on shell start and on every `cd`.

## Apply changes

1. Edit the files above.
2. Run `cmux reload-config`.
3. Run `zsh ~/.config/cmux/name-workspaces-by-folder.zsh` to re-sort now.

## Known limits

- Manual drag reordering is undone on the next `cd`.
- New tabs sort in on the next `cd`, not when they open.
- cmux has no bold option for tab names.
