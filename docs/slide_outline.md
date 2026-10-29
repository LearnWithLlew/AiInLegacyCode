# AI in Legacy Code: slide outline

Follows `slides/AiInLegacyCode.pptx`. Slide numbers in brackets.

## Title [1]
AI in Legacy Code: Small Steps, Deterministic Tools, Reusable Context

## Types of knowledge [2]
Awareness → Proficiency → Fluency

## The idea [3]
We are going to clean up some code.

## Which repo? [4]
1. CsvHelper: C#, CSV reading and writing
1. FluentValidation: C#, validation rules
1. Serilog: C#, structured logging
1. Apache Commons Text: Java, string utilities

## Augmented coding patterns, Lada Kesseler [5]
The patterns map, with three patterns highlighted:
1. Knowledge Checkpoint (12)
1. Offload Deterministic (14)
1. Knowledge Document (2)

## Knowledge Checkpoint [6–7]
1. Pattern 12 [6]
1. Arlo's Commit Notation: risk and intention on every commit [7]

## Offload Deterministic [8–11]
1. Pattern 14 on the map, then on its own [8–9]
1. `./tools/` [10]
1. `create-commit-message.sh`: the commit notation as a script [11]

## Knowledge Document [12–13]
Pattern 2 on the map, then on its own.

## Extract deterministic [14–19]
Overview [14], then one slide each:
1. Committers [15]
1. BuildAndTest [16]
1. Analyzers [17]
1. Refactoring tools [18]
1. Detectors [19]

## Fast feedback: the quick check [20]

## Sensors for code smells [21]
Habit Hooks: runs your linters, then turns each violation into a coaching guide the agent can act on.
github.com/habit-hooks/habit-hooks

## Internal documents: extract knowledge [22]

## Thank you [23]
QR code and link to github.com/isidore/Talks/blob/master/AiInLegacyCode.md

## Hidden [24–25]
Style guide and design philosophy for the deck.
