# Habit Hooks Setup: Java

How to set up [Habit Hooks](https://github.com/habit-hooks/habit-hooks) on a Java repo.
Worked on Solr (Gradle) and Apache Commons Text (Maven). The config files are in
[`kit/habit-hooks/java/`](../kit/habit-hooks/java/).

## Install (once per machine)

1. `uv tool install --force habit-hooks --with habit-hooks-java`
   A forced install replaces every plugin, so add a `--with` for each plugin you already use.
1. `brew install pmd jscpd`

## Set up the repo

1. Copy `kit/habit-hooks/java/.habit-hooks/` and `kit/habit-hooks/java/.jscpd.json` to the repo root.
1. Copy `kit/tools/run-habit-hooks.sh` to `tools/` (it is already set to `PLUGIN=java`).
1. Run `habit-hooks init`. It should report nothing missing.
1. Run `tools/run-habit-hooks.sh --all`. It exits 1 whenever it finds smells; that is not a failure.
1. Copy `kit/InternalDocuments/habit-hooks.md` into the repo and fill in the details below.
1. Commit.

## What it finds

1. From the Java plugin (PMD): methods over 12 statements, cyclomatic complexity of 10 or more,
   4 or more parameters, nesting deeper than 3, unused locals and imports, empty catches.
1. From the generic plugin: files over 200 lines, and duplication (jscpd).

## What the config changes, and why

1. `config.toml` scans `**/*.java` minus build output (`target/` for Maven; add `build/` for Gradle).
1. If PMD can't parse a file, the whole run fails. Exclude that file in `config.toml` with a `!` pattern.
   Solr needed three test files excluded.
1. `.jscpd.json` scans from the repo root in `weak` mode, so license headers don't count as duplication.
   It also ignores `import` lines, so shared import blocks aren't reported.
1. `.habit-hooks/generic/sensors/` replaces the jscpd sensor. The stock one reports the whole repo's
   duplication on every run; this one keeps only clones touching the files you asked about.

## Watch for

1. A stale `JAVA_HOME` or an old Maven. Let the build scripts pick the right versions themselves.
1. Deliberate duplication, such as deprecated classes kept next to their replacements.
   Write it down in `habit-hooks.md` so the sweep leaves it alone.
1. Apache projects run RAT, which fails on new files without a license header.
   Exclude the new files from RAT and mark them `export-ignore` in `.gitattributes`.
