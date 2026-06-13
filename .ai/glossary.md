# Glossary

This glossary contains the main domain terms. Its purpose is to keep project vocabulary consistent across code, tests,
and AI-assisted work.

## DiffBlock
DiffBlock is a raw change region found by comparing the before and after versions of the same file. It marks the
part of the file where the two versions do not match.

## Span
Span is a contiguous range of lines on one side of a diff block (before or after). It contains the full line range of 
that side within the change region.

## Hunk
Hunk is a structured analysis unit built from a change region. It consists of left and right spans and carries
additional attributes used for analysis, inspection, and navigation.

## ColumnSpec
ColumnSpec is a parsed representation of a line taken from a span inside a hunk. It extracts structured column
attributes from that line and makes them easy to access.

## Fragment
Fragment is the minimal unit of operation and interaction. It combines the parsed line attributes from column spec with
the common attributes of its hunk.

## FragmentBundle
FragmentBundle is a collection of fragments grouped together for analysis. It represents the local input state used by
rules and heuristics.

## Rule
Rule is a candidate generator. It inspects fragments and proposes possible hypotheses.

## Hypothesis
Hypothesis is a possible correspondence between two fragments. It forms the raw candidate space before evaluation.

## Component
Component is a connected group of competing hypotheses. It isolates local uncertainty so it can be resolved
independently.

## Heuristic
Heuristic is an evaluator of a candidate relation. It attaches evidence to links but does not create new candidates.

## Link
Link is a normalized candidate relation between two fragments. Multiple hypotheses for the same pair collapse into
a single link.

## Evidence
Evidence is an interpretable signal attached to a link. It supports or weakens a candidate relation.

## Refinement
Refinement is a domain-level adjustment that improves or narrows an interpretation. It helps turn a rough candidate
into a more precise one.

## Lens
Lens is an evaluator that inspects a link in the context of the current analysis. It contributes to interpretation
by scoring or classifying candidate relations.

## Context
Context is a collection of links used during analysis and evaluation.

## Decision
Decision is a consistent interpretation of a component. It selects a conflict-free subset of links.

## Preset
Preset is a predefined collection of domain objects, usually rules or heuristics, used to configure analysis behavior.