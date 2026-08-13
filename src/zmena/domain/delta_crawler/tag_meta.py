class TagMeta:
    def __init__(self, command):
        self.command = command

    def __repr__(self):
        return "TagMeta"

    def name(self):
        return self.command.show_tag()

    def annotation(self):
        return self.command.show_tag()
