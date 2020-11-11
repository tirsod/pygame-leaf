print("found me!")

import pygame
from classes import *
import scenes

pygame.init()

background_modes = BackgroundModes


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


class MonitorText(GameObject):
    valuetomonitor = None
    position = (0, 0)

    def update(self):
        render_text(self.valuetomonitor(), self.getposition(), 0)

    def getposition(self):
        return (Engine.screen.get_width()*self.position[0], Engine.screen.get_height()*self.position[1])


def init():
    Engine.bg = Background()
    Engine.scenemanager = SceneManager(scenes.scenes)
    Engine.scenemanager.go_to("default")
    Engine.timemanager = TimeManager()
    Engine.fontmanager = FontManager()


def start_game(width, height):
    Engine.screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
    Engine.game_running = True
    main_loop(Engine.screen)


def tick(fps):
    Engine.deltaTime = Engine.clock.tick(60)/1000


def render_background():
    Engine.bg.render(Engine.screen)


def display():
    pygame.display.flip()


def instantiate(obj, x=0, y=0):
    if Engine.scenemanager.scene != None:
        return Engine.scenemanager.scene.add(obj, x, y)
    else:
        print("No scene is loaded. Cannot instantiate objects into an empty scene.")


def update_scene():
    if Engine.scenemanager.scene != None:
        Engine.scenemanager.scene.update()
    else:
        print("No scene is loaded. Game closed.")
        Engine.game_running = False


def get_time_12hour():
    return Engine.timemanager.get_time_12hour()


def add_monitor_text(function, position, fontsize, fontnumber):
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


def render_text(text, xy=(0,0), fontnumber=0):
    s = Engine.fontmanager.fonts[fontnumber].render(str(text), True, (255, 255, 255))
    draw_surface(s, xy)


def main_loop(screen):
    while Engine.game_running:
        Engine.timemanager.update()
        tick(Engine.framerate)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                Engine.game_running = False    
        render_background()
        update_scene()
        display()
    pygame.quit()

init()