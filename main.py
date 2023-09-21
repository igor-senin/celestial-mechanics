import pygame

from typing import List


pygame.init()
Width, Height = pygame.display.Info().current_w, pygame.display.Info().current_h
Window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# colors
White = (255, 255, 255)
Black = (0, 0, 0)

pygame.display.set_caption("Celestial Mechanics")


class System:
    # TODO
    pass


class CelestialBody:
    # TODO : constants
    G = 6.67428e-11
    """
    Характеристики небесных тел:
        координата x
        координата y

        радиус
        масса

        модуль скорости
        вектор скорости
    """
    def __init__(self, start_x, start_y, radius, mass, colour):
        self.x_coord = start_x
        self.y_coord = start_y
        self.radius = radius
        self.mass = mass

        self.colour = colour
        self.trace = []  # List of (x, y, timestamp)

        # TODO: velocity and forces


    def update_position(self, objects):
        # TODO
        pass

    def draw(self, window, draw_line):
        if len(self.trace) > 2:
            # TODO: draw trace
            pass

        pygame.draw.circle(window, self.colour, (self.x_coord, self.y_coord), self.radius)


class Earth(CelestialBody):
    """
    Временный костыль; неподвижный объект
    """
    def update_position(self, objects: List[CelestialBody]):
        # do nothing
        pass


def do_main_cycle(bodies: List[CelestialBody]):
    run = True
    clock = pygame.time.Clock()
    draw_line = True

    while run:
        clock.tick(60)
        Window.fill(Black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            #  TODO

        for body in bodies:
            body.update_position(bodies.copy().remove(body))
            body.draw(Window, draw_line)

        pygame.display.update()

    pygame.quit()
        

def main_cycle():
    earth = Earth(
            start_x=0,
            start_y=0,
            radius=6.378 * 10**6,
            mass=5.9736 * 10**24,
            colour=White
            )

    moon = CelestialBody(  # TODO
            start_x=1.0,
            start_y=1.0,
            radius=earth.radius/10.0,
            mass=earth.mass/100.0,
            colour=White
            )

    do_main_cycle([earth, moon])


if __name__ == '__main__':
    main_cycle()
