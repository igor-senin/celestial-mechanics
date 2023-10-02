import graphics
from graphics import CelestialBody
from system import System
from physical_laws import PhysicalLaws

import pygame

from typing import List

from decimal import *
from math import sqrt
import time


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


def case_3_bodies():
    Coeff = 3.844 * 10**(9) / (graphics.Height / 2.0)

    earth = CelestialBody(
            coordinates=[Decimal(Coeff * graphics.Width / 2.0),
                         Decimal(Coeff * graphics.Height / 2.0)],
            velocity=[Decimal(-250.0), Decimal(150.0)],
            weight=Decimal(5.9742 * 10**24),
            radius=Decimal(6.378 * 10**6),
            id=1,
            colour=graphics.Blue,
            visible_radius=40.0
            )

    moon = CelestialBody(
            coordinates=[Decimal(Coeff * graphics.Width / 2.0),
                         Decimal(0.0)],
            velocity=[Decimal(300.0), Decimal(150.0)],
            weight=earth.weight,
            radius=Decimal(float(earth.radius)/10.0),
            id=2,
            colour=graphics.White,
            visible_radius=20.0
            )

    mercury = CelestialBody(
            coordinates=[Decimal(Coeff * 1500.0), Decimal(Coeff * 500.0)],
            velocity=[Decimal(150.0), Decimal(-200.0)],
            weight=earth.weight,
            radius=Decimal(float(earth.radius)/10.0),
            id=3,
            colour=graphics.Red,
            visible_radius = 25.0
            )

    do_main_cycle([earth, moon, mercury], Coeff)

def case_solar_system():
    Coeff = 1.4959787 * 10**12 / (graphics.Height / 2.0)

    sun = CelestialBody(
            coordinates=[Decimal(Coeff * graphics.Width / 2.0),
                         Decimal(Coeff * graphics.Height / 2.0)],
            velocity=[Decimal(0.0), Decimal(0.0)],
            weight=Decimal(1.98892 * 10**33),
            radius=Decimal(6.378 * 10**6),
            id=1,
            colour=graphics.Yellow,
            visible_radius=70.0
            )

    moon = CelestialBody(
            coordinates=[Decimal(Coeff * 50), Decimal(Coeff * 50)],
            velocity=[Decimal(1000.0), Decimal(200.0)],
            weight=Decimal(7.36 * 10**22),
            radius=Decimal(float(sun.radius)/10.0),
            id=2,
            colour=graphics.White,
            visible_radius=20.0
            )

    mars = CelestialBody(
            coordinates=[Decimal(Coeff * 0.0), Decimal(Coeff * 500.0)],
            velocity=[Decimal(750.0), Decimal(300.0)],
            weight=Decimal(6.39 * 10**23),
            radius=Decimal(float(sun.radius)/10.0),
            id=3,
            colour=graphics.Red,
            visible_radius = 25.0
            )

    earth = CelestialBody(
            coordinates=[Decimal(Coeff * 500.0), Decimal(Coeff * 500.0)],
            velocity=[Decimal(100000.0), Decimal(100000.0)],
            weight=Decimal(5.9742 * 10**24),
            radius=Decimal(float(sun.radius)/10.0),
            id=4,
            colour=graphics.Blue,
            visible_radius = 30.0
            )

    do_main_cycle([sun, earth, moon, mars], Coeff)


def case_2_bodies():
    Coeff = 3.844 * 10**(9) / (graphics.Height / 2.0)

    earth = CelestialBody(
            coordinates=[Decimal(Coeff * graphics.Width / 2.0),
                         Decimal(Coeff * graphics.Height / 2.0)],
            velocity=[Decimal(0), Decimal(0)],
            weight=Decimal(5.9736 * 10**24),
            radius=Decimal(6.378 * 10**6),
            id=1,
            colour=graphics.Blue,
            visible_radius=20.0
            )

    moon = CelestialBody(
            coordinates=[Decimal(Coeff * graphics.Width / 2.0), Decimal(Coeff * 0)],
            velocity=[Decimal(-200), Decimal(0)],
            weight=Decimal(7.3477 * 10**22),
            radius=Decimal(earth.radius) / Decimal(10.0),
            id=2,
            colour=graphics.White,
            visible_radius=20.0
            )
    print(Decimal(Coeff * graphics.Height / 2.0))
    do_main_cycle([earth, moon], Coeff)


def case_2_bodies_parabola():
    Coeff = 3.844 * 10**(9) / (graphics.Height / 2.0)

    earth = CelestialBody(
            coordinates=[Decimal(Coeff * graphics.Width),
                         Decimal(Coeff * graphics.Height / 3.0)],
            velocity=[Decimal(-200), Decimal(0)],
            weight=Decimal(5.9736 * 10**24),
            radius=Decimal(6.378 * 10**6),
            id=1,
            colour=graphics.Blue,
            visible_radius=20.0
            )

    moon = CelestialBody(
            coordinates=[Decimal(Coeff * 0.0),
                         Decimal(Coeff * 2.0*graphics.Height/3.0)],
            velocity=[Decimal(200), Decimal(0)],
            weight=Decimal(5.9736 * 10**24),
            radius=Decimal(earth.radius) / Decimal(10.0),
            id=2,
            colour=graphics.White,
            visible_radius=20.0
            )
    print(Decimal(Coeff * graphics.Height / 2.0))
    do_main_cycle([earth, moon], Coeff)


def main_cycle():
    graphics.init()
    getcontext().prec = 80

    #case_3_bodies()

    #case_solar_system()

    #case_2_bodies()

    case_2_bodies_parabola()
