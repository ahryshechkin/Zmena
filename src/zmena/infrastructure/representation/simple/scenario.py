from difflib import SequenceMatcher

from zmena.domain.model.hunk import Hunk
from zmena.domain.model.span import Span
from zmena.domain.types.tag import Tag
from zmena.infrastructure.representation.color import Color
from zmena.infrastructure.representation.simple.base import ReportSimple


class ReportScenario(ReportSimple):
    def __init__(self, scenario):
        super().__init__(
            f"SCE-{scenario.sce_id} - {scenario.name.upper()}",
            [
                ("action", ">", "7"),
                ("fingerprint", ">", "11"),
                ("lineno", ">", "6"),
                ("left", "<", len(max(scenario.before, key=len, default=None))),
                ("lineno", ">", "6"),
                ("right", "<", len(max(scenario.after, key=len, default=None))),
            ],
            [],
        )
        self.scenario = scenario
        self.sm = SequenceMatcher()

    def body(self):
        self.sm.set_seqs(self.scenario.before, self.scenario.after)
        for tag, slo, shi, tlo, thi in self.sm.get_opcodes():
            left = Span(self.scenario.before, slo, shi)
            right = Span(self.scenario.after, tlo, thi)
            hunk = Hunk(tag, left, right)
            if tag == Tag.EQUAL:
                for idx in range(hunk.left_range()):
                    self.show_line(idx, hunk)
            elif tag == Tag.REPLACE:
                for idx in range(hunk.height()):
                    self.show_line(idx, hunk)
            elif tag == Tag.INSERT:
                for idx in range(hunk.right_range()):
                    self.show_line(idx, hunk)
            elif tag == Tag.DELETE:
                for idx in range(hunk.left_range()):
                    self.show_line(idx, hunk)

    def show_line(self, offset, hunk):
        line = (
            f"{hunk.kind().value:>7} | "
            f"{hunk.fingerprint():>11} | "
            f"{hunk.left_lineno(offset):>6} | "
            f"{hunk.left_line(offset):<{self.width_left()}} | "
            f"{hunk.right_lineno(offset):>6} | "
            f"{hunk.right_line(offset):<{self.width_right()}}"
        )

        print(self.colorize(hunk.kind(), f"| {line} |"))

    def colorize(self, tag, text):
        colors = {
            Tag.DELETE: Color.RED,
            Tag.EQUAL: Color.GRAY,
            Tag.INSERT: Color.GREEN,
            Tag.REPLACE: Color.YELLOW,
        }

        return f"{colors[tag].value}{text}{Color.RESET.value}"

    def width_left(self):
        return len(max(self.scenario.before, key=len, default=None))

    def width_right(self):
        return len(max(self.scenario.after, key=len, default=None))
