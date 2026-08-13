from difflib import SequenceMatcher

from zmena.domain.semantic_engine.core.hunk import Hunk
from zmena.domain.semantic_engine.core.span import Span
from zmena.domain.semantic_engine.types.tag import Tag
from zmena.infrastructure.representation.ansi_color import ANSIColor
from zmena.infrastructure.representation.layouts.basic import BasicReport


class ScenarioReport(BasicReport):
    def __init__(self, message):
        super().__init__(
            f"{message.kind}-{message.label} - {message.name.upper()}",
            [
                ("action", ">", "7"),
                ("fingerprint", ">", "11"),
                ("lineno", ">", "6"),
                ("left", "<", len(max(message.before, key=len))),
                ("lineno", ">", "6"),
                ("right", "<", len(max(message.after, key=len))),
            ],
            [],
        )
        self.message = message
        self.color = ANSIColor()
        self.sm = SequenceMatcher()

    def body(self):
        self.sm.set_seqs(self.message.before, self.message.after)
        for tag, slo, shi, tlo, thi in self.sm.get_opcodes():
            left = Span(self.message.before, slo, shi)
            right = Span(self.message.after, tlo, thi)
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
            f"{hunk.kind():>7} | "
            f"{hunk.fingerprint():>11} | "
            f"{hunk.left_lineno(offset):>6} | "
            f"{hunk.left_line(offset):<{self.width_left()}} | "
            f"{hunk.right_lineno(offset):>6} | "
            f"{hunk.right_line(offset):<{self.width_right()}}"
        )

        print(self.color.style_text(hunk.kind(), f"| {line} |"))

    def width_left(self):
        return len(max(self.message.before, key=len))

    def width_right(self):
        return len(max(self.message.after, key=len))
