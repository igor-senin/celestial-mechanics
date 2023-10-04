import graphics
import examples
from graphics import CelestialBody
from system import System
from physical_laws import PhysicalLaws

import pygame

from typing import List

from decimal import *
from math import sqrt


def do_main_cycle(bodies: List[graphics.CelestialBody], scale_coeff):
    clock = pygame.time.Clock()
    run = True

    phl = PhysicalLaws()
    main_system = System(phl, bodies)

    while run:
        clock.tick(60)
        graphics.draw_universe()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

            #  TODO

        for i in range(2):
            main_system.RecalculateSystem()

        for b in main_system.GetBodies():
            b.draw(scale_coeff)

        graphics.draw_weight_center(main_system, scale_coeff)

        graphics.display_update()

    pygame.quit()


def main_cycle():
    graphics.init()
    getcontext().prec = 80

    #case_3_bodies()

    #case_solar_system()
    do_main_cycle(*examples.case_2_bodies_parabola())

    #case_2_bodies_parabola()
