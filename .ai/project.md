## Project

Zmena is a project designed to understand schema evolution by tracking schema changes across Git commits.


## Goal

It aims to detect user intent behind DDL changes and generate explainable SQL migrations from those changes.


## Core Principles

- Git is the source of truth for schema evolution
- No live database is required to understand schema evolution
- Raw diffs are input material, not the final answer
- The project focuses on semantic interpretation, not textual comparison
- The goal is to generate explainable SQL migrations
- Preserve ambiguity first, resolve it later
- Localize uncertainty into independent components
- Separate candidate generation from candidate evaluation


## Tech Stack

The repository uses Python as its main implementation language.
