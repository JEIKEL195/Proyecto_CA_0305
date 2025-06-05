# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 23:32:52 2025

@author: Jeikel Navarro Solis
"""

import numpy as np
import secrets
import matplotlib as plt

class GeneradorAleatorio:
    def __init__(self):
        semilla_segura = secrets.randbits(64)
        self.__rng = np.random.default_rng(semilla_segura)

    def flotante(self, minimo=0.0, maximo=1.0):
        return self.__rng.uniform(minimo, maximo)

    def entero(self, minimo, maximo):
        return self.__rng.integers(minimo, maximo + 1)
    
    def vector_enteros(self, minimo, maximo, n):
        return self.rng.integers(minimo, maximo + 1, size=n)

    def graficar_frecuencia_enteros(self, minimo, maximo, n=1000):
        """Genera n números enteros en [minimo, maximo] y grafica su frecuencia."""
        datos = self.vector_enteros(minimo, maximo, n)
        valores, frecuencias = np.unique(datos, return_counts=True)

        plt.figure(figsize=(12, 6))
        plt.bar(valores, frecuencias, color='mediumseagreen', edgecolor='black')
        plt.title(f"Frecuencia de {n} números aleatorios en [{minimo}, {maximo}]")
        plt.xlabel("Número")
        plt.ylabel("Frecuencia")
        plt.xticks(np.arange(minimo, maximo + 1))
        plt.grid(axis='y', linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()