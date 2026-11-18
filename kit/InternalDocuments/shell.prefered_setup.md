# Shell preferred setup (Mac)

Terse baseline for the zsh tools.

## Install

```sh
brew install atuin zoxide
```

## Wire up

Add to `~/.zshrc`:

```sh
eval "$(atuin init zsh)"
eval "$(zoxide init zsh)"
```

## What each does

- **Atuin**: replaces shell history. Ctrl-R and the up arrow search it.
- **zoxide**: `z <part of folder name>` jumps to a folder you've visited before. `zi` picks one interactively.
  - `z` is a shell function made by `zoxide init`, not an alias.

## Check it works

```sh
whence -v z      # z is a shell function
zoxide --version
atuin --version
```
