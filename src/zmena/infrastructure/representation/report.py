from difflib import SequenceMatcher

from zmena.domain.model.hunk import Hunk
from zmena.domain.model.span import Span
from zmena.domain.types.tag import Tag
from zmena.infrastructure.representation.color import Color
from zmena.infrastructure.representation.composite.component import ReportComponent
from zmena.infrastructure.representation.composite.decision import ReportDecision
from zmena.infrastructure.representation.simple.brick import ReportBrick
from zmena.infrastructure.representation.simple.hypothesis import ReportHypothesis


class Report:
    def __init__(self, scenario):
        self.sce_id = f"SCE-{scenario.sce_id}"
        self.name = scenario.name.upper()
        self.src = scenario.before
        self.trg = scenario.after
        self.width_left = len(max(self.src, key=len, default=None))
        self.width_right = len(max(self.trg, key=len, default=None))
        self.sm = SequenceMatcher()

    def show_report(self):
        self.sm.set_seqs(self.src, self.trg)

        self.print_report_header()
        for tag, slo, shi, tlo, thi in self.sm.get_opcodes():
            left = Span(self.src, slo, shi)
            right = Span(self.trg, tlo, thi)
            hunk = Hunk(tag, left, right)
            if tag == Tag.EQUAL:
                for idx in range(hunk.left_range()):
                    self.print_report_line(idx, hunk)
            elif tag == Tag.REPLACE:
                for idx in range(hunk.height()):
                    self.print_report_line(idx, hunk)
            elif tag == Tag.INSERT:
                for idx in range(hunk.right_range()):
                    self.print_report_line(idx, hunk)
            elif tag == Tag.DELETE:
                for idx in range(hunk.left_range()):
                    self.print_report_line(idx, hunk)

    def print_report_header(self):
        total_len = self.width_left + self.width_right - len(self.name) + 31

        print(
            f"\n#### {self.sce_id} - {self.name} {'#' * total_len}\n"
            f"{'action':>7} | {'fingerprint':>11} | "
            f"{'lineno':>6} | {'left':<{self.width_left}} | "
            f"{'lineno':>6} | {'right':<{self.width_right}} | ",
        )
        print(
            f"{'-' * 7}-+-{'-' * 11}-+-{'-' * 6}-+-"
            f"{'-' * self.width_left}-+-{'-' * 6}-+-{'-' * self.width_right}-+",
        )

    def print_report_line(self, offset, hunk):
        line = (
            f"{hunk.kind().value:>7} | {hunk.fingerprint():>11} | "
            f"{hunk.left_lineno(offset):>6} | {hunk.left_line(offset):<{self.width_left}} | "
            f"{hunk.right_lineno(offset):>6} | {hunk.right_line(offset):<{self.width_right}} | "
        )

        print(self.colorize(hunk.kind(), line))

    def colorize(self, tag, text):
        colors = {
            Tag.DELETE: Color.RED,
            Tag.EQUAL: Color.GRAY,
            Tag.INSERT: Color.GREEN,
            Tag.REPLACE: Color.YELLOW,
        }

        color = colors[tag].value

        return f"{color}{text}{Color.RESET.value}"

    def show_bricks(self, bricks):
        report = ReportBrick(bricks)
        report.render()

    def show_hypotheses(self, hypotheses):
        report = ReportHypothesis(hypotheses)
        report.render()

    def show_components(self, components):
        report = ReportComponent(components)
        report.render()

    def show_decisions(self, decisions):
        report = ReportDecision(decisions)
        report.render()
