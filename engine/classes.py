import time
import pygame


class BackgroundModes:
    none = 0
    color = 1
    image = 2


class Background:
    mode = BackgroundModes.none
    color = (0, 0, 0)
    
    def render(self, scr):
        if self.mode == BackgroundModes.color:
            try:
                scr.fill(self.color)
            except:
                print("Invalid color")
            
    def set_color(self, rgbcolor):
        self.mode = BackgroundModes.color
        self.color = (rgbcolor[0], rgbcolor[1], rgbcolor[2])


class Positions:
    top_left = (0, 0)
    top = (0.5, 0)
    top_right = (1, 0)
    left = (0, 0.5)
    center = (0.5, 0.5)
    right = (1, 0.5)
    bottom_left = (0, 1)
    bottom = (0.5, 1)
    bottom_right = (1, 1)


class GameObject:
    x = 0
    y = 0

    def start(self):
        """do stuff when invoked"""
    def update(self):
        """do stuff"""
    def __init__(self):
        self.start()


class Scene:
    name = "default"
    objects = []

    def add(self, obj, x, y):
        newobj = obj()
        obj.x = x
        obj.y = y
        self.objects.append(newobj)
        return newobj

    def update(self):
        for gameobj in self.objects:
            gameobj.update()

    def __init__(self, name="newscene"):
        self.name = name


class SceneManager:
    scene = None
    loaded_scenes = []
    
    def go_to(self, scenename):
        for s in self.loaded_scenes:
            print(s.name)
            if s.name == scenename:
                self.scene = s
                break

    def __init__(self, scene_list):
        self.loaded_scenes = scene_list


class TimeManager:
    def update(self):
        """future"""

    def get_time_12hour(self):
        return time.strftime("%I:%M:%S %p", time.localtime())


class FontManager:
    fonts = []
    
    def load_font(self, fontname, size):
        f = pygame.font.Font(fontname, size)
        if f is None:
            f = pygame.font.Font("fonts/"+fontname, size)
        if f is None:
            f = pygame.font.SysFont(fontname, size)
        if f is None:
            print("Could not find font of name "+fontname)
        
        if f is not None:
            self.fonts.append(f)
            
    def __init__(self):
        f = pygame.font.Font(pygame.font.get_default_font(), 25)
        self.fonts.append(f)