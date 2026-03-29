from difflib import SequenceMatcher

from zmena.domain import Hunk, Span
from zmena.domain.types.tag import Tag
from zmena.infrastructure.view.color import Color


class View:
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
        total_len = self.width_left + self.width_right - len(self.name) + 28

        print(
            f"\n#### {self.sce_id} - {self.name} {'#' * total_len}\n"
            f"{'action':>7} | {'opcode':>8} | "
            f"{'lineno':>6} | {'left':<{self.width_left}} | "
            f"{'lineno':>6} | {'right':<{self.width_right}} | ",
        )
        print(
            f"{'-' * 7}-+-{'-' * 8}-+-{'-' * 6}-+-"
            f"{'-' * self.width_left}-+-{'-' * 6}-+-{'-' * self.width_right}-+",
        )

    def print_report_line(self, offset, hunk):
        line = (
            f"{hunk.kind().value:>7} | {hunk.fingerprint():>8} | "
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
        print(
            f"\n#### Bricks "
            f"{'#' * 65} \n"
            f"{'tag':>7} | {'side':>4} | {'segment':<8} | {'position':>8} | "
            f"{'name':<7} | {'type':<13} | {'constraint':<10} | ",
        )
        print(
            f"{'-' * 7}-+-{'-' * 4}-+-{'-' * 8}-+-{'-' * 8}-+-"
            f"{'-' * 7}-+-{'-' * 13}-+-{'-' * 10}-+",
        )

        for brick in bricks:
            print(brick)

    def show_hypotheses(self, links):
        print(
            f"\n#### Hypotheses "
            f"{'#' * 165} \n"
            f"{'rule':>9} | "
            f"{'####'} | "
            f"{'tag':>7} | {'side':>4} | {'segment':<8} | {'position':>8} | "
            f"{'name':<7} | {'type':<13} | {'constraint':<10} | "
            f"{'####'} | "
            f"{'tag':>7} | {'side':>4} | {'segment':<8} | {'position':>8} | "
            f"{'name':<7} | {'type':<13} | {'constraint':<10} | ",
        )
        print(
            f"{'-' * 9}-+"
            f"{'-' * 5}-+"
            f"{'-' * 8}-+-{'-' * 4}-+-{'-' * 8}-+-"
            f"{'-' * 8}-+-{'-' * 7}-+-{'-' * 13}-+-{'-' * 10}-+"
            f"{'-' * 5}-+"
            f"{'-' * 8}-+-{'-' * 4}-+-{'-' * 8}-+-"
            f"{'-' * 8}-+-{'-' * 7}-+-{'-' * 13}-+-{'-' * 10}-+",
        )

        for link in links:
            print(link)

    def show_components(self, components):
        for i, component in enumerate(components, 1):
            print(
                f"\n#### Component {i}: "
                f"hypotheses={len(component.hypotheses)}, bricks={len(component.bricks)} "
                f"{'#' * 140} \n"
                f"{'rule':>9} | "
                f"{'####'} | "
                f"{'tag':>7} | {'side':>4} | {'segment':<8} | {'position':>8} | "
                f"{'name':<7} | {'type':<13} | {'constraint':<10} | "
                f"{'####'} | "
                f"{'tag':>7} | {'side':>4} | {'segment':<8} | {'position':>8} | "
                f"{'name':<7} | {'type':<13} | {'constraint':<10} | ",
            )
            print(
                f"{'-' * 9}-+"
                f"{'-' * 5}-+"
                f"{'-' * 8}-+-{'-' * 4}-+-{'-' * 8}-+-"
                f"{'-' * 8}-+-{'-' * 7}-+-{'-' * 13}-+-{'-' * 10}-+"
                f"{'-' * 5}-+"
                f"{'-' * 8}-+-{'-' * 4}-+-{'-' * 8}-+-"
                f"{'-' * 8}-+-{'-' * 7}-+-{'-' * 13}-+-{'-' * 10}-+",
            )

            for hypothesis in component.hypotheses:
                print(hypothesis)

            print(
                f"\n#### Component {i}: "
                f"hypotheses={len(component.hypotheses)}, bricks={len(component.bricks)} "
                f"{'#' * 36} \n"
                f"{'tag':>7} | {'side':>4} | {'segment':<8} | {'position':>8} | "
                f"{'name':<7} | {'type':<13} | {'constraint':<10} | ",
            )
            print(
                f"{'-' * 7}-+-{'-' * 4}-+-{'-' * 8}-+-"
                f"{'-' * 8}-+-{'-' * 7}-+-{'-' * 13}-+-{'-' * 10}-+",
            )

            for brick in component.bricks:
                print(brick)

    def show_decisions(self, decisions):
        for i, decision in enumerate(decisions, 1):
            print(
                f"\n#### Decision {i} "
                f"{'#' * 175} \n"
                f"{'score':>7} | {'rule':>9} | "
                f"{'####'} | "
                f"{'tag':>7} | {'side':>4} | {'segment':<8} | {'position':>8} | "
                f"{'name':<7} | {'type':<13} | {'constraint':<10} | "
                f"{'####'} | "
                f"{'tag':>7} | {'side':>4} | {'segment':<8} | {'position':>8} | "
                f"{'name':<7} | {'type':<13} | {'constraint':<10} | ",
            )
            print(
                f"{'-' * 7}-+-{'-' * 9}-+"
                f"{'-' * 5}-+"
                f"{'-' * 8}-+-{'-' * 4}-+-{'-' * 8}-+-"
                f"{'-' * 8}-+-{'-' * 7}-+-{'-' * 13}-+-{'-' * 10}-+"
                f"{'-' * 5}-+"
                f"{'-' * 8}-+-{'-' * 4}-+-{'-' * 8}-+-"
                f"{'-' * 8}-+-{'-' * 7}-+-{'-' * 13}-+-{'-' * 10}-+",
            )

            for scored_link in decision:
                print(scored_link)
