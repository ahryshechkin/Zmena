from zmena.infrastructure.reporting.console.views.fragment import FragmentView


class FragmentProjection:
    def __repr__(self):
        return "FragmentProjection(projections=fragment)"

    def apply(self, fragment):
        return FragmentView(fragment)
