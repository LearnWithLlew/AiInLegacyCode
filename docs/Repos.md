| Name                | Git URL                                                                                                                             |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| CsvHelper           | [https://github.com/JoshClose/CsvHelper](https://github.com/JoshClose/CsvHelper?utm_source=chatgpt.com)                             |
| FluentValidation    | [https://github.com/FluentValidation/FluentValidation](https://github.com/FluentValidation/FluentValidation?utm_source=chatgpt.com) |
| Serilog             | [https://github.com/serilog/serilog](https://github.com/serilog/serilog?utm_source=chatgpt.com)                                     |
| Apache Commons Text | [https://github.com/apache/commons-text](https://github.com/apache/commons-text?utm_source=chatgpt.com)                             |

## Build and test times

Measured on branch `ai-prep` with the other repos building at the same time, so solo runs may be faster.

| Name                | Language     | Build | Build warnings | Tests | Full `build_and_test.sh` | Tests run              | `quick_check.sh` (one file) |
| ------------------- | ------------ | ----- | -------------- | ----- | ------------------------ | ---------------------- | --------------------------- |
| CsvHelper           | C#           | 19s   | 0              | 56s   | 75s                      | 2,749 (net10 + net8)   | 10–14s                      |
| FluentValidation    | C#           | 9s    | 0              | 4–5s  | 13s cold, 8s warm        | 890 × 3 frameworks     | 3–4s                        |
| Serilog             | C#           | 6s    | 0              | 8s    | 14s                      | 2,455 (818 × 3 + 1)    | 6–8s                        |
| Apache Commons Text | Java (Maven) | 16s   | 0 code, 3 javac option* | 26s   | 42s                      | 1,989                  | 9–12s                       |

Build warnings come from a clean Release rebuild (`dotnet build -c Release --no-incremental`) or `./mvnw clean test-compile`.
FluentValidation and Serilog treat warnings as errors, so they can't have any.

\* Commons Text: javac warns 3 times (for main and for test code) that `source`/`target` 8 is obsolete. The full static check
(`./mvnw -DskipTests`) also reports 0 Checkstyle, PMD and SpotBugs violations; its other warnings are about the tools'
own setup (PMD rules scheduled for removal, two goals skipped when offline).

## Largest source files

Top 5 non-test source files by line count, on branch `ai-prep` (after the first habit-hooks pass).

| Name                | #   | Lines | File                                                                   |
| ------------------- | --- | ----- | ---------------------------------------------------------------------- |
| CsvHelper           | 1   | 2,362 | `src/CsvHelper.Generators/RecordParser.cs`                             |
|                     | 2   | 1,663 | `src/CsvHelper/CsvWriter.cs`                                           |
|                     | 3   | 1,362 | `src/CsvHelper/CsvWriter.Parallel.cs`                                  |
|                     | 4   | 1,150 | `src/CsvHelper/CsvReader.Fields.cs`                                    |
|                     | 5   | 1,094 | `src/CsvHelper/CsvSeparatorStream.Scan.cs`                             |
| FluentValidation    | 1   | 1,199 | `src/FluentValidation/DefaultValidatorExtensions.cs`                   |
|                     | 2   | 599   | `src/FluentValidation/DefaultValidatorOptions.cs`                      |
|                     | 3   | 399   | `src/FluentValidation/AbstractValidator.cs`                            |
|                     | 4   | 344   | `src/FluentValidation/Internal/RuleBase.cs`                            |
|                     | 5   | 331   | `src/FluentValidation/IValidationContext.cs`                           |
| Serilog             | 1   | 1,434 | `src/Serilog/Core/Logger.cs`                                           |
|                     | 2   | 1,370 | `src/Serilog/ILogger.cs`                                               |
|                     | 3   | 1,204 | `src/Serilog/Log.cs`                                                   |
|                     | 4   | 635   | `src/Serilog/Formatting/Json/JsonValueFormatter.cs`                    |
|                     | 5   | 528   | `src/Serilog/Capturing/PropertyValueConverter.cs`                      |
| Apache Commons Text | 1   | 3,198 | `src/main/java/org/apache/commons/text/TextStringBuilder.java`         |
|                     | 2   | 2,975 | `src/main/java/org/apache/commons/text/StrBuilder.java`                |
|                     | 3   | 1,782 | `src/main/java/org/apache/commons/text/lookup/StringLookupFactory.java` |
|                     | 4   | 1,590 | `src/main/java/org/apache/commons/text/StringSubstitutor.java`         |
|                     | 5   | 1,212 | `src/main/java/org/apache/commons/text/StrSubstitutor.java`            |
