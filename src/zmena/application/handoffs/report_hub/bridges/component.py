from zmena.infrastructure.reporting.console.views.component import ComponentView


class ComponentMint:
    def __init__(self, fragment_mint, hypothesis_mint):
        self.fragment_mint = fragment_mint
        self.hypothesis_mint = hypothesis_mint

    def __repr__(self):
        return "ComponentMint(mints=component,hypothesis,fragment)"

    def issue(self, component):
        fragments = [self.fragment_mint.issue(fragment) for fragment in component.fragments]
        hypotheses = [self.hypothesis_mint.issue(hypothesis) for hypothesis in component.hypotheses]

        return ComponentView(fragments, hypotheses)
