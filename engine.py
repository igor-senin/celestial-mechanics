import graphics
from graphics import CelestialBody
from system import System
from physical_laws import PhysicalLaws

import pygame

from typing import List


from math import sqrt
import time


def do_main_cycle(bodies: List[graphics.CelestialBody]):
    clock = pygame.time.Clock()
    run = True

    phl = PhysicalLaws()
    main_system = System(phl, bodies)
    while run:
        clock.tick(120)
        graphics.draw_universe()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

            #  TODO

        main_system.RecalculateSystem()

        for b in main_system.GetBodies():
            #print(f"drawing {b.id}")
            b.draw()

        graphics.display_update()

    pygame.quit()
    return

    G = 6.6743 * 10**(-11)# * (10**(1) * 3)
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

        #main_system.RecalculateSystem()
        new_system = dict()
        for i in range(len(bodies)):
            for j in range(len(bodies)):
                if i == j:
                    continue
                cb = bodies[i]
                other = bodies[j]

                #print(f"\n\nlog: body {i}")

                dist = sqrt((cb[0] - other[0])**2 + (cb[1] - other[1])**2)

                #print(f"dist = {dist}")
                if dist < 0.000001:
                    print("too small distance")
                    continue
                rv = [(other[0] - cb[0]), (other[1] - cb[1])]

                #print(f"cb[0] = {cb[0]}, cb[1] = {cb[1]}")
                #print(f"other[0] = {other[0]}, other[1] = {other[1]}")
                #print(f"rv[0] = {rv[0]}, rv[1] = {rv[1]}")

                a = [G * other.weight * rv[0] / dist**3,
                     G * other.weight * rv[1] / dist**3]

                #print(f"a[0] = {a[0]}, a[1] = {a[1]}")

                t = 0.000001

                rnew = [cb[0] + cb.velocity[0] * t + a[0] * t**2 / 2.0,
                        cb[1] + cb.velocity[1] * t + a[1] * t**2 / 2.0]

                #print(f"vwas: {cb.velocity[0]}, {cb.velocity[1]}")

                vnew = [cb.velocity[0] + a[0] * t, cb.velocity[1] + a[1] * t]
                #print(f"vnew: {vnew[0]}, {vnew[1]}")

                new_system[i] = (rnew, vnew)
                
        for key, value in new_system.items():
            bodies[key].coordinates = value[0]
            bodies[key].velocity = value[1]

        for b in bodies:
            #print(f"drawing {b.id}")
            b.draw()

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
            coordinates=[50, 50],
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
            coordinates=[graphics.Width / 2.0,
                         graphics.Height / 2.0], velocity=[0, 0],
            weight=5.9736 * 10**22,
            radius=6.378 * 10**6,
            id=1,
            colour=graphics.Blue,
            visible_radius=40.0
            )

    moon = CelestialBody(
            coordinates=[50, 50],
            velocity=[20000, -20000],
            weight=7.348 * 10**20,
            radius=earth.radius/10.0,
            id=2,
            colour=graphics.White,
            visible_radius=20.0
            )
    do_main_cycle([earth, moon])


def main_cycle():
    graphics.init()

    #case_3_bodies()

    case_2_bodies()

    #case_solar_system()
