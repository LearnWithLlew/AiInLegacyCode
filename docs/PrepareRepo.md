# Prepare a Repo for AI-Assisted Cleanup

A checklist for repeating on another repo what we did on Solr: agent rules, fast feedback, smell
sensors, then a refactoring sweep run by subagents. Each step has a prompt you can paste; replace `<kit>` with the path to
[`kit/`](../kit/) in this repo. Commit after each step.

## 1. Clone and branch

1. [ ] Clone the repo and create a working branch.
   ```
   git clone <url> && cd <repo> && git checkout -b <branch>
   ```

## 2. Agent rules

1. [ ] Copy `AGENTS.md` rules (🍀 prefix, one question at a time, ⭐/❌ decisions, end-of-task report,
   no private memory, `1.` lists) and `build-tools/create-commit-message.sh` from [`kit/`](../kit/).
   > Copy the agent rules from `<kit>/AGENTS.md` and `<kit>/build-tools/create-commit-message.sh` into this
   > repo. Merge with any AGENTS.md/CLAUDE.md already here, keep the project's own guidance. Then commit.
1. [ ] Check: the reply starts with 🍀 and the commit message starts with `. e`.

## 3. Build and test script

1. [ ] Get a full build and test working and timed.
   > Create `build_and_test.sh` that builds and runs all tests. Run it until it works, install what
   > you need. Time the build and the tests separately and show me the numbers. Ask any questions now,
   > I'll be away from the keyboard.
1. [ ] Watch for: a stale `JAVA_HOME` or tool version; make the script pick the right one itself.
1. [ ] Record the times. If the full run is longer than a few minutes, go on to step 4.

## 4. Quick check (10–30 seconds)

1. [ ] Ask for options first.
   > The build and test script is way too slow. I want feedback in 10–30 seconds that the code builds
   > and works. Give me all your suggestions.
1. [ ] Build the one you pick.
   > Make `quick_check.sh`: compile everything, then run only the tests named after the changed
   > classes, in one build-tool call. Support `--branch <base>`. Print the time and exit code last.
   > Also write `InternalDocuments/QuickCheck.md` as if it were a skill file, terse and in plain English.
   > Commit as you go in small steps.
1. [ ] Check: it finishes in under 30 seconds on a one-file change, and exits non-zero on a broken test.
1. [ ] Watch for: `grep` with no matches killing the script under `set -e -o pipefail`; tests skipped
   by default (e.g. nightly/slow tags) that still count as a pass. Write those gaps into QuickCheck.md.

## 5. Habit-hooks setup

1. [ ] Install the tools (once per machine).
   ```
   uv tool install --force habit-hooks --with habit-hooks-<language>
   brew install pmd jscpd        # for Java
   ```
1. [ ] Configure and run it on the repo.
   > Set up habit-hooks for this repo, following `<kit>/InternalDocuments/habit-hooks.md`. Get
   > `habit-hooks init` clean and a full run working. Make `build-tools/run-habit-hooks.sh` that checks
   > the tools are installed but never reinstalls them. Write `InternalDocuments/habit-hooks.md`.
1. [ ] Watch for:
   1. Files the parser cannot handle: one failure aborts the whole run, so exclude them in
      `.habit-hooks/config.toml`.
   1. jscpd scanning only `src`, counting license headers as duplication, or reporting the whole repo
      on every run: add a root `.jscpd.json` in `weak` mode and a scoped jscpd sensor override
      (copy `.habit-hooks/generic/sensors/` from Solr).
1. [ ] Tell habit-hooks.md to run `./quick_check.sh` after each smell fix.
   > Modify habit-hooks.md to use quick_check after each fix.

## 6. Keep the internal docs out of release checks

1. [ ] Run the repo's full static check (e.g. `gradlew check -x test`) once. If a license or
   source-header check fails on `InternalDocuments/`, exclude the folder there and from source
   releases (Solr: `gradle/validation/rat-sources.gradle` and `.gitattributes` `export-ignore`).

## 7. The process file

1. [ ] Adapt the sweep process.
   > Make a version of `<kit>/InternalDocuments/processes/habit-hooks.process.md` for this repo.
1. [ ] Make sure it says:
   1. One subagent per file, one at a time.
   1. One fix → format → `quick_check.sh` → commit `- r`. Revert with `git revert`, never `reset --hard`.
   1. Don't pipe `quick_check.sh` into `tail`; that hides its exit code.
   1. Run the module's full static check (e.g. `:<module>:check -x test`) after each file.
   1. Fixes keep behavior: same order of side effects, locking, null handling; no public or
      protected signature changes.
   1. Possible bugs are logged in `InternalDocuments/habit-hooks-sweep-findings.md`, not fixed.

## 8. The sweep

1. [ ] Start with the biggest files, excluding tests.
   > Make a pass at habit hooks now. Start with the biggest files and exclude tests. Read
   > `InternalDocuments/processes/habit-hooks.process.md` and do each file in a subagent.
1. [ ] Let it run unattended.
   > Continue as much as possible. I'll be away from the keyboard; do as many files as you can.
1. [ ] Add to every subagent prompt:
   1. At most 5 commits per file; at most 3 if one quick check takes over 5 minutes.
   1. If the build daemon runs out of memory, stop it (`./gradlew --stop`) and retry.
1. [ ] Check each subagent's claimed bugs and "equivalent" refactors yourself before trusting them.
1. [ ] Stop when you want to.
   > OK, pause after this.

## 9. Before pushing

1. [ ] Run `./build_and_test.sh` once on the whole branch; the quick checks only ran name-matched tests.
1. [ ] Review the `- r` commits, e.g. `git log --oneline <base>..HEAD` and `git show -w <sha>`.
1. [ ] Turn confirmed entries in the findings file into issues with their own tests and fixes,
   on a separate branch.
