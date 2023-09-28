from body import Body

import pygame


# colors
White = (255, 255, 255)
Black = (0, 0, 0)

def init():
    pygame.init()

    global Width, Height, Window
    Width, Height = pygame.display.Info().current_w, pygame.display.Info().current_h
    Window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    pygame.display.set_caption("Celestial Mechanics")

def display_update():
    pygame.display.update()

def draw_universe():
    Window.fill(Black)

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

        self.trace = []  # List of (x, y, timestamp)

    def draw(self):
        pygame.draw.circle(Window,
                           self.colour, 
                          (self.coordinates[0], self.coordinates[1]), 
                           self.visible_radius)

        if len(self.trace) > 2:
            for i in range(self.trace):
                pass
            pass

