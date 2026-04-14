## Zmena

[![Lines of Code](https://img.shields.io/endpoint?url=https://tokei.kojix2.net/badge/github/ahryshechkin/Zmena/lines)](https://tokei.kojix2.net/github/ahryshechkin/Zmena)
[![Hits-of-Code](https://hitsofcode.com/github/ahryshechkin/Zmena?branch=main&label=Hits+of+Code)](https://hitsofcode.com/github/ahryshechkin/Zmena/view?branch=main)
[![Coverage](https://codecov.io/gh/ahryshechkin/Zmena/branch/main/graph/badge.svg)](https://codecov.io/gh/ahryshechkin/Zmena)

Writing SQL migrations by hand... again?
- Multiple environments.
- Multiple releases.
- Endless ALTER TABLE statements.

There must be a better way!


## Overview

Zmena understands SQL schema evolution from Git history and turns DDL diffs into SQL migrations.


## Key Idea

Zmena treats SQL files in Git as the source of truth.

It parses DDL, detects semantic schema changes between commits, and automatically generates migration scripts.
No raw text diffs. No live databases. No ORM metadata. No custom migration language.

This keeps schema definitions in plain SQL and fits naturally into Git-based CI and release workflows.