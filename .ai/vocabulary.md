## Vocabulary

This glossary contains the main domain terms. Its purpose is to keep project vocabulary consistent across code, tests,
and AI-assisted work.

- `ColumnSpec` is a column definition consisting of a name, a data type, and nullability.
- `Component` is a connected group of fragments and hypotheses representing a shared interpretation problem. Its
hypotheses are related through common fragments, and its heuristics provide the criteria for assessing them.
- `Context` is an original set of candidate links available as a reference during contextual refinement.
- `Decision` is a collection of scored candidate links with a non-conflicting selection of winners. A fragment may
belong to at most one winning link.
- `Evidence` is a weighted reason supporting or opposing a hypothesis. Its signal expresses direction and strength,
while its weight expresses importance.
- `Fragment` is a column occurrence within a schema diff. Its identity in the comparison includes its side, block,
position, change tag, and column properties.
- `FragmentBundle` is a collection of fragments from both sides of a schema comparison, organized by side and diff
block.
- `Heuristic` is a local assessment criterion for a hypothesis, identified by its kind. It represents one source of
evidence about a fragment pair.
- `Hunk` is a contiguous diff block consisting of a change tag and the corresponding spans in the before and after
versions.
- `Hypothesis` is a possible correspondence between a left fragment and a right fragment attributed to the rule behind
that interpretation. Either side may be a stub, representing an insertion or deletion.
- `Lens` is a contextual assessment criterion for a candidate link. Unlike a local heuristic, its perspective includes
other links in the same context.
- `Link` is a candidate correspondence between two fragments, together with its supporting and opposing evidence. Its
score expresses the combined weight of that evidence.
- `Preset` is a named category of predefined domain policies.
- `Refinement` is a contextual assessment policy composed of lenses. It represents the additional perspective supplied
by relationships among candidate links rather than by an isolated fragment pair.
- `Rule` is a policy defining which fragment relationships qualify as plausible hypotheses. Its kind identifies the
basis for those hypotheses.
- `Span` is a bounded section of a line sequence, identified by an inclusive lower boundary and an exclusive upper
boundary.