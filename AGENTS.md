# AGENTS.md

## Context

Read before changing code:

- `.ai/architecture.md` — layers and dependency direction
- `.ai/glossary.md` — domain vocabulary
- `.ai/project.md` — goal and stack
- `.ai/workflow.md` — the ten processing stages

## Code style

Rules the codebase follows consistently. Almost none of them are enforced by
tooling: `ruff` catches line length and formatting, everything below rests on
review. The single exception is the boolean argument rule, which `FBT003`
enforces. So check the rest by hand, and when a rule changes, change every
existing call site with it.

### Value carriers and behavior

Most rules below follow from one split.

| | Value carrier | Behavior |
|---|---|---|
| Classes | `Scenario`, `messages/`, `records/`, `statements/` | everything else |
| Declared as | `@dataclass` | plain `class` |
| Constructed with | named arguments | positional arguments |
| Annotations | on fields | none |
| Values are read through | fields | plain methods |

`@dataclass` appears in exactly these four categories and nowhere else, 26
classes in total. The message, record and statement categories are the
subdirectories of `application/edges/*/`; `Scenario` is in
`application/scenario.py`. Introducing `@dataclass` outside them, or writing a
plain class inside them, breaks the assumption the other rules rest on.

### Rules

#### Instantiate behavior positionally

Pass behavior objects positionally. Name the value at the call site instead:
`after.name` already says it is a name, and `name=after.name` only repeats it.
The named form of the call in `Plan.derive` reaches 118 characters against a
limit of 100 and expands to five nested lines.

#### Name boolean arguments, always

The one carve-out from the rule above, and the only rule here that a tool
enforces. A boolean literal is unmistakable on its own but not at the call
site: `AddColumnStatement(after.name, after.data_type, False)` reads `False`
as if it modified the data type. Write `nullable=False`. `FBT003` rejects the
positional form outright, so this is not a matter of taste. Value carriers
already name every argument, so the two rules never conflict.

#### Name the arguments of value carriers

Records, messages, statements and `Scenario` take named arguments. They are
dataclasses whose fields are read by name throughout the reporting code, and
naming keeps a call site readable when several fields hold similar values.

#### Deserialize fixtures with `**` unpacking

The accepted exception to the two rules above. `SEFixtureCatalog` and
`MFFixtureCatalog` read a JSON object into a record or a statement. Rewriting
them positionally would obscure which field is which.

#### Annotate dataclass fields only

Method parameters, return types and plain class attributes carry no
annotations. All 77 annotations in `src/` are on dataclass fields.

#### Call accessors, do not declare properties

Read a value by calling it: `link.score()`, `hunk.kind()`, `decision.winners()`.
`@property` is not used in `src/`.

#### Assign constructor state before collaborators

Attributes derived from parameters first, internally constructed objects last.
Reading top to bottom then follows the order in which the object is really
built.

#### Order dunder methods

`__init__`, `__repr__`, `__str__`, `__lt__`, then public methods. No class
deviates.

#### Define `__repr__` on every class

Unless it is an enum or inherits one from a base class. The body is
`ClassName(field=value,...)`, with no space after the comma. The console views
that are rendered directly define `__str__` instead.

#### Print identifying fields only

Collapse collections to `len(...)` and print only what identifies the object,
so a payload never reaches the output.

Some families share a shortened prefix on purpose:

| Family | Told apart by | Example |
|---|---|---|
| Report layouts | a field key | `Report(basic=...)` |
| Fixture catalogs | nothing, identical bodies | `FixtureCatalog(root_dir=...)` |

`BasicReport` and `CompositeReport` print `Report(...)`; `MFFixtureCatalog` and
`SEFixtureCatalog` print `FixtureCatalog(...)`. `FragmentRecord` and `Preset`
each exist in two packages under the same name with identical bodies, so the
prefix is correct in both.

#### Write no comments

No explanatory comments anywhere. The only two in `src/` are commented-out
calls in `run_delta_crawler.py`. The only suppressions are `S603` for
subprocess calls and `TC001` where `src/` imports no third-party package.
