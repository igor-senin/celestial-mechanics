import pygame

from typing import List
import body
import physical_laws
import system

pygame.init()
Width, Height = pygame.display.Info().current_w, pygame.display.Info().current_h
Window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# colors
White = (255, 255, 255)
Black = (0, 0, 0)

pygame.display.set_caption("Celestial Mechanics")


class CelestialBody(body.Body):
    def __init__(self, weight, radius, direction, coordinates, id, colour):
        # TODO may be optimize
        self.weight = weight
        self.radius = radius 
        self.direction = direction
        self.coordinates = coordinates
        self.id = id

        self.colour = colour
        self.trace = []  # List of (x, y, timestamp)

    def draw(self, window, draw_line):
        pygame.draw.circle(window, self.colour, 
                          (self.coordinates[0] / 10 ** 22, self.coordinates[1] / 10 ** 22), 
                           self.radius)

        if len(self.trace) > 2:
            # TODO: draw trace
            pass


def do_main_cycle(bodies: List[CelestialBody]):
    run = True
    clock = pygame.time.Clock()
    draw_line = True

    accuracy = 0.00001
    centre = [0., 0.]
    phl = physical_laws.PhysicalLaws()
    main_system = system.System(accuracy, centre, phl, bodies)

    while run:
        clock.tick(60)
        Window.fill(Black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            #  TODO

        main_system.RecalculateSystem()

        for i in range(main_system.GetBodiesCount()):
            body = main_system.GetBody(i)
            body.draw(Window, draw_line)

        pygame.display.update()

    pygame.quit()
        

def main_cycle():
    earth = CelestialBody(
            coordinates=[0, 0],
            direction=[0, 0],
            weight=5.9736 * 10**24,
            radius=6.378 * 10**6,
            id=1,
            colour=White
            )

    moon = CelestialBody(
            coordinates=[10 ** 20, 10 ** 20],
            direction=[0, 0],
            weight=earth.weight/100.0,
            radius=earth.radius/10.0,
            id=2,
            colour=White
            )

    do_main_cycle([earth])


if __name__ == '__main__':
    main_cycle()
