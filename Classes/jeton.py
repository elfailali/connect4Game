class Jeton:
    def __init__(self, color="red"):
        if color is None:
            self.color = "red"
        else:
            self.color = color

    def getColor(self):
        return str(self.color)

