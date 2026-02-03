### `Rule`
- proposes hypotheses

### `Link`
- records hypotheses
- represents a hypothesis about correspondence between Bricks, proposed by a Rule

### `Component`
- a connected, closed subgraph of Links in which all involved Bricks are mutually dependent and must be interpreted together
- a set of Bricks
- a set of Links between them
- isolates uncertainty

### `Decision`
- a consistent interpretation of a Component that produces semantic Statements
- a consistent interpretation of a Component that selects, rejects or combines Links and produces semantic conclusions
- resolves uncertainty
- a subset of Links such that:
  - each Brick participates in no more than one interpretation
  - there are no logical conflicts (delete + rename at the same time, etc.)

### `Statement`
- the result of decoding a Decision in terms of DDL
- emits meaning
