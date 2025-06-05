# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 23:32:52 2025

@author: Jeikel Navarro Solis
"""

import numpy as np
import secrets

class GeneradorAleatorio:
    def __init__(self):
        semilla_segura = secrets.randbits(64)
        self.__rng = np.random.default_rng(semilla_segura)

    def flotante(self, minimo=0.0, maximo=1.0):
        return self.__rng.uniform(minimo, maximo)

    def entero(self, minimo, maximo):
        return self.__rng.integers(minimo, maximo + 1)
