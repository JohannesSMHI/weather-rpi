#!/usr/bin/env python3
"""
Created on 2021-11-21 15:13

@author: johannes
"""
from weather_rpi.utils import round_value


class TempFormatter:
    """Doc."""

    def __init__(self, serie, _):
        self.serie = serie

    def __call__(self):
        """Return temperature in Celcius.

        Converts fahrenheit to Celsius.
        """
        temps = (self.serie - 32) / 1.8
        return temps.apply(lambda x: round_value(x, nr_decimals=2))
