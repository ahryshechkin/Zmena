# Contributing to Zmena

Thank you for your interest in contributing to **Zmena**!  
We welcome bug reports, feature requests, documentation improvements, and code contributions.

Please take a moment to read this guide before opening an Issue or Pull Request.

---

## Getting started

1. Fork the repository
2. Create a new branch from `main`
3. Make your changes
4. Open a Pull Request

---

## Naming Convention

### PR Title

Pull Request title follows this format:

```
[ZM-<issue-id>] Short Description
```


### Branch Name

Use the following format:

```
zm-<issue-id>-short-description
```

Examples:
- zm-0001-add-new-parser
- zm-0002-handle-empty-input

Guidelines:
- Use lowercase letters and hyphens only
- Avoid spaces or special characters


### Commit Message

This project complies with the following convention:

```
<type>: short description
```

Examples and allowed types:
- `feat`: add base parser interface
- `fix`: handle empty input
- `test`: add parser unit tests
- `refactor`: extract common logic
- `docs`: add parser usage example

Guidelines:
- Use **imperative mood** (`add`, `handle`, `extract`)
- Keep commits focused and meaningful
- Avoid mixing unrelated changes in one commit
