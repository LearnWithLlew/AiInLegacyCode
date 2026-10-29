# Habit Hooks Setup: C#

How to set up [Habit Hooks](https://github.com/habit-hooks/habit-hooks) on a C# repo.
Worked on CsvHelper, FluentValidation and Serilog. The config files are in
[`kit/habit-hooks/csharp/`](../kit/habit-hooks/csharp/), taken from Serilog.

## Install (once per machine)

1. `uv tool install --force habit-hooks --with habit-hooks-csharp`
   A forced install replaces every plugin, so add a `--with` for each plugin you already use.
1. `brew install jscpd jq`
1. A .NET SDK. The comment tool in the csharp plugin needs the .NET 8 runtime or later.

## Set up the repo

1. Copy `kit/habit-hooks/csharp/.habit-hooks/` and `kit/habit-hooks/csharp/.jscpd.json` to the repo root.
1. In `.habit-hooks/config.toml`, set `files` to where the code lives (default `src/` and `test/`).
1. In `.habit-hooks/csharp/sensors/roslyn.toml`, set the project path and framework on the `warnings=` line.
1. Copy `kit/tools/run-habit-hooks.sh` to `tools/` and set `PLUGIN=csharp`.
1. Run `habit-hooks init`. It doesn't detect C#; the config already turns the csharp plugin on.
1. Run `tools/run-habit-hooks.sh --all`. It exits 1 whenever it finds smells; that is not a failure.
1. Copy `kit/InternalDocuments/habit-hooks.md` into the repo and fill in the details below.
1. Commit.

## What it finds

1. From the csharp plugin: comments, and Roslyn analyzer warnings for unused members, parameters and
   imports, and high complexity.
1. From the generic plugin: files over 200 lines, and duplication (jscpd).
1. Not covered: long methods, deep nesting, too many parameters, swallowed exceptions.
   Write that gap into `habit-hooks.md` so the agent looks for those itself.

## What the config changes, and why

1. `csharp/sensors/comment.toml` drops license headers and `///` XML doc comments.
   Those docs are the library's published API documentation, and often required by the build.
   On CsvHelper this cut one file from 137 comment findings to 51.
1. `csharp/sensors/roslyn.toml` replaces the stock analyzer sensor. Most libraries treat warnings as
   errors and turn no metric rules on, so the stock sensor finds nothing. This one builds one project
   in Debug with all analyzers on, just for habit-hooks; the normal build is untouched.
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
