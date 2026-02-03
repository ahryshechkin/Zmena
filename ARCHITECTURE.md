### `Rule`
- proposes hypotheses

### `Link`
- records hypotheses
- A Link represents a hypothesis about correspondence between bricks, proposed by a Rule

### `Component`
- a set of Bricks
- a set of Links between them
- isolates uncertainty

### `Decision`
- resolves uncertainty
- a subset of Links such that:
  - each Brick participates in no more than one interpretation
  - there are no logical conflicts (delete + rename at the same time, etc.)

### `Statement`
- the result of decoding a Decision in terms of DDL
- emits meaning
