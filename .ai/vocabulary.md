## Vocabulary

This glossary contains the main domain terms. Its purpose is to keep project vocabulary consistent across code, tests,
and AI-assisted work.

- `DiffBlock` is a region where the before and after versions of the same file differ. It is a documentation-only
concept used to define spans, hunks, and fragments, with no separate abstraction in the code.
- `ColumnSpec` is a parsed column definition consisting of a name, a data type, and nullability. It extracts these
properties from a SQL column-definition line. It describes the column independently of its position or role in a
DiffBlock.
- `Component` is a connected group of fragments and hypotheses representing a shared interpretation problem. Its
hypotheses are connected by shared fragments and assessed using heuristics.
- `Context` is a shared source of information for lenses during refinement. It provides a broader view of candidate
links, so each link can be reassessed in relation to others rather than in isolation.
- `Decision` is a set of scored candidate links and selected winners for a component. The winners do not conflict with
each other. Each fragment may belong to at most one winning link.
- `Evidence` is a weighted reason for or against a hypothesis. It contributes to the score of a link and explains why
the link is more or less likely to be correct.
- `Fragment` is a column definition tied to a specific line on one side of a DiffBlock. It combines column properties
with tag, block, position, side. It serves as the basic unit for column correspondence hypotheses.
- `FragmentBundle` provides a convenient interface for working with a collection of fragments.
- `Heuristic` is a criterion for the local assessment of a hypothesis. It provides evidence for or against a
correspondence based on the two fragments alone.
- `Hunk` is a structured representation of a DiffBlock, with a left span and a right span. The two spans describe the
same region of change but may contain different numbers of lines.
- `Hypothesis` is a possible correspondence between a left fragment and a right fragment proposed by a specific rule.
Either side may be a stub to represent a possible insertion or deletion.
- `Lens` is a criterion for the global reassessment of a candidate link during refinement. It provides additional
evidence based on relationships with other links in the same context.
- `Link` is a candidate correspondence between two fragments, with evidence for and against it. The combined evidence
determines the score used to compare the link with other candidates and select winners.
- `Preset` is a predefined collection of rules, heuristics, lenses, or other domain entities for a particular
processing stage. It provides a ready-to-use configuration for that stage.
- `Refinement` is a global reassessment of candidate links through a set of lenses. It adds evidence from the wider
context to the initial local assessment, before the selection of winners.
- `Rule` is a criterion for possible correspondences between fragments. It provides the basis for new hypotheses
without assessing how likely they are to be correct
- `Span` is a continuous range of lines on the left (before) or right (after) side of a DiffBlock. Either span may be
empty for an insertion or deletion.