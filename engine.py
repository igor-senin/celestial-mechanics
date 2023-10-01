import graphics
from graphics import CelestialBody
from system import System
from physical_laws import PhysicalLaws

import pygame

from typing import List

from decimal import *
from math import sqrt
import time


# meters in one pixel
Coeff = 7.11852 * 10**6 # TODO: float -> Decimal
#Coeff = 1.0

def do_main_cycle(bodies: List[graphics.CelestialBody]):
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

        for i in range(100):
            main_system.RecalculateSystem()

        for b in main_system.GetBodies():
            b.draw(Coeff)

        graphics.draw_weight_center(main_system, Coeff)

        graphics.display_update()

    pygame.quit()


def case_3_bodies():
    earth = CelestialBody(
            coordinates=[graphics.Width / 2.0,
                         graphics.Height / 2.0], velocity=[0, 500],
            weight=5 * 10**18,
            radius=6.378 * 10**6,
            id=1,
            colour=graphics.Blue,
            visible_radius=40.0
            )

    moon = CelestialBody(
            coordinates=[graphics.Width / 2.0, 0],
            velocity=[500, 0],
            weight=earth.weight,
            radius=earth.radius/10.0,
            id=2,
            colour=graphics.White,
            visible_radius=20.0
            )

    mercury = CelestialBody(
            coordinates=[1500, 500],
            velocity=[250, 300],
            weight=earth.weight,
            radius=earth.radius/10.0,
            id=3,
            colour=graphics.Red,
            visible_radius = 25.0
            )

    do_main_cycle([earth, moon, mercury])

def case_solar_system():
    sun = CelestialBody(
            coordinates=[graphics.Width / 2.0,
                         graphics.Height / 2.0],
            velocity=[0, 0],
            weight=5 * 10**20,
            radius=6.378 * 10**6,
            id=1,
            colour=graphics.Yellow,
            visible_radius=70.0
            )

    moon = CelestialBody(
            coordinates=[50, 50],
            velocity=[500, 0],
            weight=10**18,
            radius=sun.radius/10.0,
            id=2,
            colour=graphics.White,
            visible_radius=20.0
            )

    mars = CelestialBody(
            coordinates=[0, 500],
            velocity=[250, 300],
            weight=2 * 10**18,
            radius=sun.radius/10.0,
            id=3,
            colour=graphics.Red,
            visible_radius = 25.0
            )

    earth = CelestialBody(
            coordinates=[500, 500],
            velocity=[250, 300],
            weight=5* 10**18,
            radius=sun.radius/10.0,
            id=4,
            colour=graphics.Blue,
            visible_radius = 30.0
            )

#    do_main_cycle([sun, earth, moon, mars])
    do_main_cycle([sun, earth])


def case_2_bodies():
    earth = CelestialBody(
            coordinates=[Decimal(Coeff * graphics.Width / 2.0),
                         Decimal(Coeff * graphics.Height / 2.0)],
            velocity=[Decimal(50000), Decimal(0)],
            weight=Decimal(5.9736 * 10**24),
            radius=Decimal(6.378 * 10**6),
            id=1,
            colour=graphics.Blue,
            visible_radius=20.0
            )

    moon = CelestialBody(
            coordinates=[Decimal(Coeff * graphics.Width / 2.0), Decimal(Coeff * 0)],
            velocity=[Decimal(-50000), Decimal(0)],
            weight=earth.weight,
            radius=Decimal(earth.radius) / Decimal(10.0),
            id=2,
            colour=graphics.White,
            visible_radius=20.0
            )
    do_main_cycle([earth, moon])


def main_cycle():
    graphics.init()
    getcontext().prec = 800

    #case_3_bodies()

    case_2_bodies()

    #case_solar_system()
