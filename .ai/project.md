## Project

Zmena is a tool designed to understand database schema evolution by analyzing how SQL files change across Git
commits. It treats the schema as a continuously evolving artifact and uses its history to identify and explain how
the database structure changes over time.


## Goal

The primary goal is to generate explainable, semantically meaningful migrations rather than mechanically translating
textual diffs into SQL statements. A change in the schema files does not necessarily correspond directly to a single
database operation. The same textual difference may represent fundamentally different intentions. For example,
a column may have been:
- renamed rather than removed and recreated;
- moved without any semantic change;
- modified in place;
- removed intentionally;
- replaced by another column;
- or introduced as part of a larger structural change.

Because multiple interpretations may be plausible, Zmena must reason about the meaning of a change rather than relying
solely on textual similarity. The analysis should therefore identify possible interpretations, evaluate competing
hypotheses, and produce the migration that best explains the observed schema evolution.

The resulting migrations should be:
- `Semantically Meaningful` They should reflect the likely intent behind the schema change.
- `Explainable` The reasoning behind a migration should be understandable and traceable.
- `Deterministic` The same schema history should produce the same result.


## Tech Stack

- `Python 3.14+` is the implementation language.
- `sqlglot` is a dependency for working with SQL syntax.
- `uv` manages the Python environment and dependencies.
- `unittest` is used for automated tests.
- `coverage` measures test coverage.
- `Ruff` provides linting and formatting.
- `pre-commit` runs repository checks.
- `Git` stores the schema history from which changes are analyzed.
