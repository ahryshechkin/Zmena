from zmena.application.handoffs.test_suite.snapshots.lightweight_link import LightweightLinkSnapshot


class LightweightLinkBridge:
    def translate(self, link):
        return LightweightLinkSnapshot(left=link.left, right=link.right)
