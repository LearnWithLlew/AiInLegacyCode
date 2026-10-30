# Habit Hooks Setup: C#

How to set up [Habit Hooks](https://github.com/habit-hooks/habit-hooks) on a C# repo.
Worked on CsvHelper, FluentValidation and Serilog. The config files are in
[`kit/habit-hooks/csharp/`](../kit/habit-hooks/csharp/).

## Install (once per machine)

1. `uv tool install --force habit-hooks --with habit-hooks-csharp`
   A forced install replaces every plugin, so add a `--with` for each plugin you already use.
   The plugin is [habit-hooks-csharp](https://pypi.org/project/habit-hooks-csharp/) on PyPI
   ([source](https://github.com/isidore/HabitHooksCsharp)).
1. `brew install jscpd`
1. The .NET 8 SDK or later.

## Set up the repo

1. Copy `kit/habit-hooks/csharp/.habit-hooks/` and `kit/habit-hooks/csharp/.jscpd.json` to the repo root.
1. In `.habit-hooks/config.toml`, set `files` to where the code lives, and set `--project` to the solution or
   project the roslyn sensor should build (or delete those lines if the folder has only one).
1. Copy `kit/tools/run-habit-hooks.sh` to `tools/` and set `PLUGIN=csharp`.
1. Run `tools/run-habit-hooks.sh --all`. It exits 1 whenever it finds smells; that is not a failure.
1. Copy `kit/InternalDocuments/habit-hooks.md` into the repo and fill in the details below.
1. Commit.

## What it finds

1. **smells** (no build): 4 or more parameters, 12 or more statements in a method, nesting 3 deep,
   cyclomatic complexity of 10 or more, empty catch blocks. Same thresholds as the Java plugin.
1. **comment**: comments that could be names. License headers and `///` doc comments are skipped by default;
   `[sensors.comment] args = ["--include-file-header", "--include-doc-comments"]` turns them back on.
1. **roslyn**: unused members, fields, parameters, variables and imports, and high coupling. It builds in Debug
   with the analyzers turned on, even when the project treats warnings as errors, without changing its files.
1. From the generic plugin: files over 200 lines, and duplication (jscpd).

## What the kit config adds, and why

1. `.jscpd.json` scans from the repo root (`"."`) in `weak` mode, so comments don't count as duplication.
   Scanning from `src` breaks the next item.
1. `generic/sensors/` replaces the jscpd sensor. The stock one reports the whole repo's duplication on
   every run; this one keeps only clones touching the files you asked about.

## Watch for

1. Duplication you can't remove without changing public API, such as `Logger` and the static `Log`
   in Serilog. Write it down in `habit-hooks.md` so the sweep leaves it alone.
1. `dotnet format` that rewrites whole files (line endings, indentation). If it isn't clean on the
   untouched repo, tell the process file to format by hand.
1. Missing runtimes for some target frameworks. Set `DOTNET_ROLL_FORWARD=Major` in the build scripts,
   or note which frameworks aren't tested locally.
