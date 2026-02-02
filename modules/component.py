class Component:
    def __init__(self):
        self.links = set()
        self.bricks = set()


    def add(self, link):
        self.links.add(link)
        self.bricks.add(link.left)
        self.bricks.add(link.right)
