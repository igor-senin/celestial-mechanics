import graphics
from graphics import CelestialBody
from system import System
from physical_laws import PhysicalLaws

import pygame

from typing import List


def do_main_cycle(bodies: List[graphics.CelestialBody]):
    clock = pygame.time.Clock()
    run = True

    accuracy = 0.00001
    centre = [0., 0.]

    phl = PhysicalLaws()
    main_system = System(accuracy, centre, phl, bodies)

    while run:
        clock.tick(60)
        graphics.draw_universe()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            #  TODO

        main_system.RecalculateSystem()

        for b in bodies:
            b.draw()

        graphics.display_update()

    pygame.quit()
        

def main_cycle():
    graphics.init()

    earth = CelestialBody(
            coordinates=[0, 0],
            direction=[0, 0],
            weight=5.9736 * 10**24,
            radius=6.378 * 10**6,
            id=1,
            colour=graphics.White,
            visible_radius=100.0
            )

    moon = CelestialBody(
            coordinates=[10 ** 20, 10 ** 20],
            direction=[0, 0],
            weight=earth.weight/100.0,
            radius=earth.radius/10.0,
            id=2,
            colour=graphics.White,
            visible_radius=10.0
            )

    do_main_cycle([earth, moon])
