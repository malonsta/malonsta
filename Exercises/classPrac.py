class Cars:
    def __init__(self, colors, mileage):
        self.colors = colors
        self.mileage = mileage

    def soundCheck(self, sound):
        return f"Car makes {self.sound} sound"


class Benz(Cars):
    def soundCheck(self, sound='grrrr'):
        return super.soundCheck(sound)


