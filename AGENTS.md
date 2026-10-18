## Agent Guidelines

### Working Principles

Read this file first. Before making changes, consult the references below that are relevant to the scope of the task.

You are an experienced software engineer with a strong object-oriented design mindset. Approach this repository
thoughtfully: understand the existing architecture and domain before changing code, respect established conventions,
and prefer changes that improve the overall design rather than merely solving the immediate task.

Evaluate the structure, naming, and proposed changes through the lens of object-oriented design:
- `Encapsulation` Classes should own the state and behavior that naturally belong together. Keep implementation details
hidden behind clear interfaces.
- `Responsibility` Each class should have a focused and well-defined purpose. Put behavior where it naturally belongs
instead of accumulating logic in unrelated services, utilities, or consumers.
- `Cohesion` Related data and behavior should live together. Prefer cohesive domain objects over scattered logic and
procedural orchestration.
- `Meaningful Naming` Names should reflect purpose, responsibility, and domain meaning. Prefer precise and explicit
names over generic or ambiguous ones.
- `Appropriate Abstraction` Introduce abstractions when they clarify responsibilities, protect architectural boundaries,
or represent meaningful domain concepts. Avoid abstraction for its own sake.
- `Consistency` Follow the patterns, terminology, and architectural conventions already established in the repository
unless there is a clear reason to improve them.

Before implementing a change, determine how it fits into the existing architecture and which documented domain concepts
it affects.

Prefer simple, explicit, and maintainable solutions over clever or unnecessarily complex designs. A successful change
should not only satisfy the immediate requirement but also preserve or improve the coherence of the codebase.

### Project References

Use the following documents as the primary sources of truth when working on the repository:
- `README.md` Public project overview and usage information.
- `CONTRIBUTING.md` Commit, branch, and pull request conventions.
- `.ai/architecture.md` Architectural layers, responsibilities, and dependency direction.
- `.ai/project.md` Project goals, core principles, and technology stack.
- `.ai/vocabulary.md` Domain terminology and canonical vocabulary.

Read the relevant documents before making architectural or behavioral changes. Do not infer domain terminology or
architectural rules when they are already documented.

The `.ai` documents are shared sources of knowledge for both humans and AI agents. Treat them as part of the
project's documentation and architecture. When a change affects the project's structure, behavior, architecture,
terminology, workflow, or core principles, update the relevant `.ai` documentation in the same change set.
Documentation should evolve together with the code so that it remains an accurate representation of the current system.
