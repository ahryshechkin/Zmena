## Vocabulary

This glossary contains the main domain terms. Its purpose is to keep project vocabulary consistent across code, tests,
and AI-assisted work.

### Delta Crawler

**Delta Crawler** is a discovery module for changed files and other artifacts. It identifies relevant changes and
provides the before and after versions for further processing without interpreting their meaning.

### SQL Intake

**SQL Intake** is a harmonization layer between raw file (or artifact) contents and the following modules. Its input
may vary in formatting and include content beyond SQL table definitions. It extracts the relevant schema information
and provides it in a consistent format for further processing.

### Semantic Engine

**Semantic Engine** is the core of schema change interpretation. It represents possible column correspondences as
hypotheses, assesses them through heuristics and lenses, and provides decisions with scored candidate links and
non-conflicting winning links.

- `ColumnSpec` is a parsed representation of a column profile provided by SQL Intake. It contains a name, a data type,
and nullability. It describes the column independently of any comparison context.
- `Component` is a connected group of fragments and hypotheses representing a shared interpretation problem. Its
hypotheses are connected by shared fragments and assessed using heuristics.
- `Context` is a source of information for lenses during refinement. It provides a broader view of candidate links. So
each link can be reassessed in relation to others rather than in isolation.
- `Decision` is a set of scored candidate links and selected winning links for a component. The winners do not
conflict with each other. Each fragment may belong to at most one winning link.
- `DiffBlock` is a region where the before and after versions of the same file (or artifact) differ. It is a
documentation-only concept used to define hunks, spans, and fragments with no separate abstraction in the code.
- `Evidence` is a weighted reason for or against a hypothesis. It contributes to the score of a link and explains why
the link is more or less likely to be correct.
- `Fragment` is a structured representation of a single column on one side of a diff block. It combines column
properties from column spec with tag, block, position, and side from a hunk and its span. It serves as the basic unit
for hypotheses about how columns correspond between the before and after versions.
- `FragmentBundle` is a collection of fragments with a shared interface for access by side and block. It provides the
fragment groups needed to propose new hypotheses.
- `Heuristic` is a criterion for the local assessment of a hypothesis. It provides evidence for or against a
correspondence based on two fragments.
- `Hunk` is a structured representation of a diff block with left and right spans. The two spans describe the same
region of change but may contain different numbers of lines.
- `Hypothesis` is a possible correspondence between left and right fragments proposed by a specific rule. Either side
may be a stub to represent a possible insertion or deletion.
- `Lens` is a criterion for the global reassessment of a candidate link during refinement. It provides additional
evidence based on relationships with other links in the same context.
- `Link` is a candidate correspondence between two fragments with evidence for and against it. The score is the sum of
all evidence scores. It is used to compare the link with other candidates and select winners.
- `Preset` is a predefined collection of heuristics, lenses, rules, or other domain entities for a particular
processing stage. It provides a ready-to-use configuration for that stage.
- `Refinement` is a global reassessment of candidate links through a set of lenses. It adds evidence from the wider
context to the initial local assessment before the selection of winners.
- `Rule` is a criterion for possible correspondence between fragments. It provides the basis for new hypotheses without
assessing how likely they are to be correct.
- `Span` is a continuous range of lines on the left (before) or right (after) side of a diff block. Either span may be
empty for an insertion or deletion.
- `Step` is a domain operation that represents one stage of semantic interpretation with a specific input, output, and
responsibility. Steps belong to the domain. Their execution order belongs to the application layer.
  - `FragmentBuilder` is a step from textual differences to fragments. Each fragment contains the properties of one
  column and its location in a diff block. The output contains no hypotheses or links between fragments.
  - `HypothesisProposer` is a step from fragments to possible correspondences. Its rules provide hypotheses about the
  meaning of the observed differences for later assessment.
  - `ComponentComposer` is a step from individual hypotheses to connected components. Each component contains
  hypotheses connected through shared fragments and forms a separate scope for assessment.
  - `DecisionResolver` is a step from components to decisions. Each decision contains scored candidate links. Heuristics
  provide the initial local assessment, and lenses add a global reassessment. The links are then ready for winner
  selection.

### Migration Forge

**Migration Forge** is the bridge from interpreted schema changes to migration statements. It provides concrete
operations for column additions, deletions, renames, and changes to data types or nullability.
