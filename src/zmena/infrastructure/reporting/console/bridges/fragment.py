from zmena.infrastructure.reporting.console.views.fragment import FragmentView


class FragmentBridge:
    def __repr__(self):
        return "FragmentBridge(bridges=fragment)"

    def translate(self, fragment):
        return FragmentView(fragment)
