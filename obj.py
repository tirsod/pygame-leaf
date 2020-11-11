from engine import *

class backgroundChanger(GameObject):
    r = 0
    g = 0
    b = 0

    def update(self):
        Engine.bg.set_color((self.r, self.g, self.b))
        if self.b < 255:
            self.b += 50*Engine.deltaTime
        else:
            self.b = 0