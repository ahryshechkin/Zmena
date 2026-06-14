## Architecture

The project follows a layered architecture with three main areas: `application`, `domain`, and `infrastructure`. The
layers have different responsibilities and should depend on each other only in one direction.


## Layer Overview

### `application`

The layer coordinates the work of the system. It contains use cases and the sequence of steps needed to run an analysis
from start to finish.

Its responsibilities are:
- preparation of input for analysis
- orchestration of the analysis pipeline
- transfer of data between domain objects
- collection and return of the execution result

This layer should contain application services and use cases, but not business rules.

### `domain`

The layer is the heart of the system. It describes the problem space and contains the rules used to reason about it.

Its responsibilities are:
- representation of the main domain entities
- grouping of competing relations into local structures
- definition of rules for generating, evaluating, and refining relations
- accumulation and interpretation of evidence
- production of stable decisions from available evidence

This layer must remain independent of outer layers and external concerns.

### `infrastructure`

The layer contains everything that interacts with the outside world.

Its responsibilities are:
- reading data from files or other external sources
- provision of entry points for running the system
- rendering reports and textual output
- adaptation of external data into objects that the application can use


## Dependency direction

Dependencies should follow this direction:
- `application` may depend on `domain`
- `domain` must not depend on the upper layers
- `infrastructure` may depend on `application` and `domain`

In short:
- orchestration lives in `application`
- business rules live in `domain`
- I/O and presentation live in `infrastructure`

If a piece of code answers one of these questions, it should usually belong to the corresponding layer:
- "What should happen next?" → `application`
- "What is valid?" → `domain`
- "How do we read, write, or display it?" → `infrastructure`
