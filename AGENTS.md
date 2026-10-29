# AGENTS.md

`kit/AGENTS.md` is a template to copy into other repos; these rules are for this repo.

## Deterministic slides and PDFs

Before committing a `.pptx` or `.pdf`, run [Determinize](https://github.com/SimonCropp/Determinize) on it,
so saving the same content again produces the same bytes and git only records real changes.

1. Install once: `dotnet tool install -g Determinize`
1. Rewrite in place: `determinize slides/AiInLegacyCode.pptx`
1. Check without writing: `determinize slides/AiInLegacyCode.pptx --check` (exit code 1 means not deterministic)

Put the path before the options.
