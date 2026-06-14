## Architecture

The project follows a layered architecture with three main areas: `application`, `domain`, and `infrastructure`.


## Layers

### `application`

The layer coordinates the work of the system. It contains use cases and the sequence of steps needed
to run an analysis from start to finish.

#### Responsibilities

- prepare input for analysis
- run the analysis pipeline
- pass data between domain objects
- collect the final result of execution

### `domain`

The layer is the heart of the system. It describes the problem space and the rules used to reason about it.

#### Responsibilities

- represent the main domain entities and value objects
- define the rules for generating, evaluating, and refining relations
- accumulate and interpret evidence
- group competing relations into local structures
- produce stable decisions from the available evidence

### `infrastructure`

The layer contains everything that interacts with the outside world.

#### Responsibilities

- read data from files or other external sources
- provide entry points for running the system
- render reports and textual output
- adapt external data into objects that the application can use


## Dependency direction

Dependencies should follow this direction:
- `application` may depend on `domain`
- `domain` must not depend on the upper layers
- `infrastructure` may depend on `application` and `domain`
