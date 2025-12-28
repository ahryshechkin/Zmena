# Zmena

> **Detects changes in SQL files and generates corresponding SQL statements**  

## Overview

Zmena is a Git-native tool that analyzes SQL files containing DDL statements and generates SQL expressions reflecting the actual changes.

It compares SQL files between two Git commits, without just comparing raw text or connecting to a live database.

## Key Idea

Zmena works with SQL files, not databases.

It does not require ORM metadata or a special migration language.  
Instead, it interprets what changed in the DDL statements and generates SQL to apply those changes.
