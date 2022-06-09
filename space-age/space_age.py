from typing import Dict
import typing

planet_age_factor: typing.Mapping[str, int] = {
    'mercury': 0.2408467,
    'venus': 0.61519726,
    'earth': 1,
    'mars': 1.8808158,
    'jupiter': 11.862615,
    'saturn': 29.447498,
    'uranus': 84.016846,
    'neptune': 164.79132,
}

SECONDS_IN_A_YEAR = 60 * 60 * 24 * 365.25


class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds


    def _on_planet(self, planet: str):
        print(planet)
        return round(
            (self.seconds / SECONDS_IN_A_YEAR) / planet_age_factor[planet],
            2
        )


def make_on_planet(planet: str):
    def fn(self):
        return self._on_planet(planet)

    return fn


for planet in planet_age_factor:
    setattr(SpaceAge, f'on_{planet}', make_on_planet(planet))
