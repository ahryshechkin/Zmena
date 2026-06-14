## Workflow

Below is the workflow that explains how the application works.

#### 1. Raw diff block detection
The input before and after SQL versions are compared, and contiguous change regions are identified. These regions are
the starting point for the rest of the workflow.

#### 2. Span extraction
Each change region is reduced to the relevant left and right spans. This step isolates the line ranges that participate
in the change and prepares them for further processing.

#### 3. Hunk assembly
The extracted spans are combined into a hunk. This gives the workflow a structured unit that carries the change region
forward into fragment generation.

#### 4. Fragment generation
Fragment is created from the common attributes of a hunk and a column spec. Fragments are the base objects used by the
whole analysis pipeline.

#### 5. Rule-based hypothesis generation
At the first stage, rules are applied to the fragments.

Each rule:
- inspects fragments from the left and right sides
- determines whether a relation between them is possible
- creates a hypothesis when the relation is acceptable

This produces a pool of hypotheses. The pool may contain both correct and noisy candidates, but the main goal is
to preserve every potentially valid correspondence.

#### 6. Graph construction
Hypotheses are then used to build a graph:
- fragments are vertices
- hypotheses are edges

The graph makes it possible to:
- detect connected components
- isolate mutually related and competing fragments
- limit the next stages to local regions of uncertainty

#### 7. Link normalization
The main hypothesis processing stage begins after graph formation. Hypotheses are traversed sequentially, and for
every unique fragment pair from a hypothesis a link is created if it does not already exist. A link is the normalized
representation of a candidate relation between two fragments.

#### 8. Heuristic evaluation
Each link is evaluated by a set of heuristics.

Heuristics:
- analyze fragment pairs
- may add evidence
- do not have to add evidence in every case

Evidence is an interpretable signal that supports or weakens the link.

#### 9. Context-aware refinement
After the initial heuristic pass, links can be revisited in a broader context.

This stage:
- uses surrounding context to reassess links
- applies lenses as context-aware evaluators
- adds new evidence when the local result is still incomplete or uncertain
- helps stabilize the final interpretation

#### 10. Decision-making
After the initial heuristic pass and contextual refinement, a decision selects a conflict-free subset of links.

This stage:
- resolves remaining conflicts between competing links
- filters out incompatible candidates
- produces a stable interpretation for the component


## Summary

- Raw diff regions are detected first
- Relevant line ranges are isolated and assembled into a structured diff unit
- Fragments are created from common hunk and column spec attributes
- Rules constrain the search space by generating candidates
- The graph decomposes the problem into independent components
- Hypothesis traversal produces unique fragment pairs
- Heuristics add interpretable evidence
- Contextual refinement re-evaluates links with lenses and surrounding context
- Decisions select a conflict-free subset of links
