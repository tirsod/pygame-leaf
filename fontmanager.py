import pygame

class FontManager():
    fonts = []
    
    def load_font(self, fontname, size):
        f = pygame.font.Font(fontname, size)
        if (f == None):
            f = pygame.font.Font("fonts/"+fontname, size)
        if (f == None):
            f = pygame.font.SysFont(fontname, size)
        if (f == None):
            print("Could not find font of name "+fontname)
        
        if (f != None):
            self.fonts.append(f)
            
    def __init__(self):
        f = pygame.font.Font(pygame.font.get_default_font(), 25)
        self.fonts.append(f)