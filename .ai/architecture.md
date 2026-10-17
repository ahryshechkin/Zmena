## Architecture

Zmena uses a layered architecture with three areas: `domain`, `application`, and `infrastructure`. This separates the
logic for understanding schema changes from the code that coordinates how the system works and interacts with the
outside world.


## Layers

### Domain

The domain contains the logic for interpreting schema changes. It defines core concepts, possible relationships between
them, and rules for choosing the most likely explanation for the observed differences. The domain must not depend on
file formats, input sources, or output methods.

For example, when a column is removed and another is added to the same table, the domain determines whether the new
column replaces the old one or is unrelated to it.

**In short**: The domain decides what a schema change means.

### Application

The application layer coordinates the processing workflow. It prepares the data, runs the required domain operations in
the correct order, and collects the results.

For example, the application runs modules in a specific order and with selected parameters to support different
scenarios and produce a consistent result.

**In short**: The application coordinates how data is processed.

### Infrastructure

The infrastructure layer handles interactions with the outside world. It includes code for reading input data,
accessing external sources, and presenting results. Infrastructure converts external data into a format the application
can use and presents the results in the required format. It does not decide what a schema change means.

For example, loading a scenario from a catalog and printing an analysis report to the console belong to this layer.

**In short**: Infrastructure handles input, output, and external systems.


## Dependency Direction

Source-code dependencies point inward:

`infrastructure` → `application` → `domain`

The rules are simple:
- domain must not depend on application or infrastructure;
- application may depend on domain, but not on infrastructure;
- infrastructure may depend on both application and domain.

These rules keep the core logic independent of external systems and make it easier to change or test individual layers.
