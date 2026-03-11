## Zmena

[![Hits‑of‑Code](https://hitsofcode.com/github/octocat/Hello‑World)](https://hitsofcode.com/github/ahryshechkin/Zmena/view)

Writing SQL migrations by hand... again?
- Multiple environments.
- Multiple releases.
- Endless ALTER TABLE statements.

There must be a better way!


## Overview

Zmena understands semantic changes in SQL schemas and generates corresponding SQL migrations.


## Key Idea

Zmena works with SQL files, not databases.

It does not require ORM metadata or a special migration language.  
Instead, it interprets what changed in the DDL statements and generates SQL to apply those changes.

It compares SQL files between two Git commits without just comparing raw text or connecting to a live database.