import pygame
import background

import scenemanager
import scenes

import timemanager

import fontmanager

pygame.init()

background_modes = background.BACKGROUNDMODES

class Engine():
    game_running = False
    screen = None
    scenemanager = None
    timemanager = None
    fontmanager = None
    bg = None
    framerate = 60
    clock = pygame.time.Clock()
    deltaTime = 0

class Positions():
    topleft = 0
    top = 1
    topright = 2
    left = 3
    center = 4
    right = 5
    bottomleft = 6
    bottom = 7
    bottomright = 8

class Gameobject():
    x = 0
    y = 0
    def start(self):
        """do stuff when invoked"""
    def update(self):
        """do stuff"""
    def __init__(self):
        self.start()
    
class MonitorText(Gameobject):
    valuetomonitor = None
    position = 0
    def update(self):
        render_text(self.valuetomonitor(), self.getposition(), 0)
    def getposition(self):
        if (self.position == Positions.center):
            return (Engine.screen.get_width()/2, Engine.screen.get_height()/2)

def init(width, height):
    Engine.screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
    Engine.bg = background.Background()
    Engine.scenemanager = scenemanager.SceneManager()
    Engine.scenemanager.load("default", scenes.scenes)
    Engine.timemanager = timemanager.TimeManager()
    Engine.fontmanager = fontmanager.FontManager()

def start_game():
    Engine.game_running = True
    main_loop(Engine.screen)
    
def tick(fps):
    Engine.deltaTime = Engine.clock.tick(60)/1000
    
def render_background():
    Engine.bg.render(Engine.screen)
     
def display():
    pygame.display.flip()

def instantiate(obj, x = 0, y = 0):
    if Engine.scenemanager.scene != None:
        return Engine.scenemanager.scene.add(obj, x, y)
    else:
        print("No scene is loaded. Cannot instantiate objects into an empty scene.")

def update_scene():
    if (Engine.scenemanager.scene != None):
        Engine.scenemanager.scene.update()
    else:
        print("No scene is loaded. Game closed.")
        Engine.game_running = False

def get_time_12hour():
    return Engine.timemanager.get_time_12hour()

def add_monitor_text(function, position, fontsize, fontnumber):
    '''Create an object that monitors and renders the value of a variable'''
    mt = instantiate(MonitorText)
    mt.valuetomonitor = function
    mt.position = position
    
def draw_surface(surface, xy = (0, 0), centered = True):
    size = surface.get_size()
    nx = xy[0]
    ny = xy[1]
    if centered:
        nx -= (size[0]/2)
        ny -= (size[1]/2)
    Engine.screen.blit(surface, (nx, ny))
    
def render_text(text, xy = (0 ,0), fontnumber = 0):
    s = Engine.fontmanager.fonts[fontnumber].render(str(text), True, (255, 255, 255))
    draw_surface(s, xy)
    
def main_loop(screen):
    while(Engine.game_running):
        Engine.timemanager.update()
        tick(Engine.framerate)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                Engine.game_running = False    
        render_background()
        update_scene()
        display()
    pygame.quit()
    
    