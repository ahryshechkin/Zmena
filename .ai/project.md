## Project Overview

Zmena is a project designed to understand schema evolution by tracking schema changes across Git commits. It aims to
detect user intent behind DDL changes and generate explainable SQL migrations from those changes.

It operates on SQL in version control. No live database is required to understand schema evolution. The project focuses
on semantic interpretation rather than raw textual diffs.

The repository uses Python as its main implementation language.
