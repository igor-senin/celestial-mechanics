from body import Body

import pygame

from math import floor


# colors
White = (255, 255, 255)
Blue  = (30, 144, 255)
Black = (0, 0, 0)
Red   = (255, 0, 0)
Green = (0, 200, 0)
Yellow= (255, 255, 0)

def init():
    pygame.init()

    global Width, Height, Window
    Width, Height = pygame.display.Info().current_w, pygame.display.Info().current_h
    Window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    
    global Universe
    Universe = pygame.Surface((Width, Height), pygame.SRCALPHA)

    pygame.display.set_caption("Celestial Mechanics")

def display_update():
    pygame.display.update()

def draw_universe():
    Window.fill(Black)
    Window.blit(Universe, (0,0))

"""
    Drawable class
"""
class CelestialBody(Body):
    def __init__(self,
                 weight,
                 radius,
                 velocity,
                 coordinates,
                 id,
                 colour,
                 visible_radius=None):
        super(CelestialBody, self).__init__(weight,
                                   radius,
                                   coordinates,
                                   velocity,
                                   id)
        self.colour = colour
        self.visible_radius = radius if visible_radius is None else visible_radius

        self.trace = []  # List of (x, y)

    def draw(self):
        pygame.draw.circle(Window,
                           self.colour, 
                          (self.coordinates[0], self.coordinates[1]), 
                           self.visible_radius)

        self.trace.append((self.coordinates[0], self.coordinates[1]))

        if len(self.trace) > 2:
            self.draw_trace()

    def draw_trace(self):
        for i in range(len(self.trace)):
            pygame.draw.circle(Universe,
                               (*self.colour, floor(100 * i / 750) + 50),
                               self.trace[i],
                               5.0)

        if len(self.trace) > 750:
            self.trace = self.trace[1:]

