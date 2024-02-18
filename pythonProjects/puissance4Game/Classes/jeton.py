class Jeton:
    def __init__(self, color=None):
        if color is None:
            self.color = "red"
        else:
            self.color = color

    def getColor(self):
        return self.color

