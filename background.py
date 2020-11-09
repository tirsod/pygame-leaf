"""Modes"""

class BACKGROUNDMODES():
    none = 0
    color = 1
    image = 2

class Background():
    mode = BACKGROUNDMODES.none
    color = (0, 0, 0)
    
    def render(self, scr):
        if self.mode == BACKGROUNDMODES.color:
            try:
                scr.fill(self.color)
            except:
                print("Invalid color")
            
    def set_color(self, rgbColor):
        self.mode = BACKGROUNDMODES.color
        self.color = (rgbColor[0], rgbColor[1], rgbColor[2])