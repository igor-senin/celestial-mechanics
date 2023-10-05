import graphics
from graphics import CelestialBody

from decimal import *
from math import sqrt


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

    return ([earth, moon, mercury], Coeff)

def case_solar_system():
    Coeff = 1.4959787 * 10**11 / (graphics.Height / 3.0)

    sun = CelestialBody(
            coordinates=[Decimal(Coeff * graphics.Width / 2.0),
                         Decimal(Coeff * graphics.Height / 2.0)],
            velocity=[Decimal(0.0), Decimal(0.0)],
            weight=Decimal(1.98892 * 10**33),
            radius=Decimal(6.378 * 10**6),
            id=1,
            colour=graphics.Yellow,
            visible_radius=40.0
            )

    earth = CelestialBody(
            coordinates=[sun.coordinates[0] - Decimal(Coeff * graphics.Width / 3.0),
                         sun.coordinates[1]],
            velocity=[Decimal(0.0), Decimal(30000.0)],
            weight=Decimal(5.9742 * 10**24),
            radius=Decimal(float(sun.radius)/10.0),
            id=4,
            colour=graphics.Blue,
            visible_radius = 10.0
            )

    moon = CelestialBody(
            coordinates=[(sun.coordinates[0] - earth.coordinates[0]) * Decimal(3.84467 * 10**8) / Decimal(1.4959787 * 10**11),
                         earth.coordinates[1]],
            velocity=[Decimal(0.0), earth.velocity[1] + Decimal(1000.0)],
            weight=Decimal(7.36 * 10**22),
            radius=Decimal(float(sun.radius)/10.0),
            id=2,
            colour=graphics.White,
            visible_radius=4.0
            )

    mars = CelestialBody(
            coordinates=[(sun.coordinates[0] - earth.coordinates[0]) * Decimal(2.28 * 10**11) / Decimal(1.4959787 * 10**11),
                         earth.coordinates[1]],
            velocity=[Decimal(0.0), Decimal(24130.0)],
            weight=Decimal(6.39 * 10**23),
            radius=Decimal(float(sun.radius)/10.0),
            id=3,
            colour=graphics.Red,
            visible_radius = 8.0
            )

    return ([sun, earth, moon, mars], Coeff)


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
    return ([earth, moon], Coeff)


def case_2_bodies_parabola():
    Coeff = 3.844 * 10**(9) / (graphics.Height / 2.0)

    earth = CelestialBody(
            coordinates=[Decimal(Coeff * graphics.Width / 4 * 3),
                         Decimal(Coeff * graphics.Height / 3.0)],
            velocity=[Decimal(-200), Decimal(0)],
            weight=Decimal(5.9736 * 10**24),
            radius=Decimal(6.378 * 10**6),
            id=1,
            colour=graphics.Blue,
            visible_radius=20.0
            )

    moon = CelestialBody(
            coordinates=[Decimal(Coeff * graphics.Width / 4),
                         Decimal(Coeff * 2.0*graphics.Height/3.0)],
            velocity=[Decimal(200), Decimal(0)],
            weight=Decimal(5.9736 * 10**24),
            radius=Decimal(earth.radius) / Decimal(10.0),
            id=2,
            colour=graphics.White,
            visible_radius=20.0
            )
    print(Decimal(Coeff * graphics.Height / 2.0))
    return ([earth, moon], Coeff)


def case_3_bodies_triangle():
    Coeff = 3.844 * 10**(9) / (graphics.Height / 2.0)

    H = graphics.Height / 3.0
    A = 2 * H / sqrt(3)

    moon1 = CelestialBody(
            coordinates=[Decimal(Coeff * graphics.Width / 2.0),
                         Decimal(Coeff * graphics.Height / 3.0)],
            velocity=[Decimal(-100), Decimal(0)],
            weight=Decimal(9 * 10**23),
            radius=Decimal(6.378 * 10**6),
            id=1,
            colour=graphics.Blue,
            visible_radius=20.0
            )

    moon2 = CelestialBody(
            coordinates=[Decimal(Coeff * (graphics.Width / 2.0 - A / 2.0)),
                         Decimal(Coeff * 2 * graphics.Height / 3.0)],
            velocity=[Decimal(50), Decimal(50 * sqrt(3.0))],
            weight=moon1.weight,
            radius=Decimal(6.378 * 10**6),
            id=2,
            colour=graphics.White,
            visible_radius=20.0
            )

    moon3 = CelestialBody(
            coordinates=[Decimal(Coeff * (graphics.Width / 2.0 + A / 2.0)),
                         Decimal(Coeff * 2 * graphics.Height / 3.0)],
            velocity=[Decimal(50), Decimal(-50 * sqrt(3.0))],
            weight=moon1.weight,
            radius=Decimal(6.378 * 10**6),
            id=3,
            colour=graphics.Red,
            visible_radius=20.0
            )
    return ([moon1, moon2, moon3], Coeff)

