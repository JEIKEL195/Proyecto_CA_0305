# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 23:32:52 2025

@author: Jeikel Navarro Solis
"""

import numpy as np
import secrets
import matplotlib.pyplot as plt

class GeneradorAleatorio:
    def __init__(self):
        ''' Inicializa una instancia del generador de números pseudoaleatorios.

        Parámetros
        ----------
        None

        Retorna
        -------
        None
        '''
        semilla_segura = secrets.randbits(64)
        self.__rng = np.random.default_rng(semilla_segura)

    def flotante(self, minimo: float = 0, maximo: float = 1):
        ''' Genera un número flotante aleatorio en el intervalo [minimo, maximo).

        Parámetros
        ----------
        minimo (float): Límite inferior del intervalo (incluido). Por defecto es 0.
        maximo (float): Límite superior del intervalo (excluido). Por defecto es 1.

        Retorna
        -------
        (float): Número aleatorio flotante en el rango [minimo, maximo).
        
        ''' 
        return self.__rng.uniform(minimo, maximo)

    def entero(self, minimo: int, maximo: int):
        ''' Genera un número entero aleatorio entre minimo y maximo (inclusive).

        Parámetros
        ----------
        minimo (int): Límite inferior del rango (incluido).
        maximo (int): Límite superior del rango (incluido).

        Retorna
        -------
        (int): Número entero aleatorio entre minimo y maximo.
        
        '''
        return self.__rng.integers(minimo, maximo + 1)
    
    def vector_enteros(self, minimo: int, maximo: int, simulaciones):
        ''' Genera un vector de números enteros aleatorios en el intervalo [minimo, maximo].

        Parámetros
        ----------
        minimo (int): Límite inferior del rango (incluido).
        maximo (int): Límite superior del rango (incluido).
        simulaciones (int): Número de valores a generar.

        Retorna
        -------
        (np.ndarray): Arreglo de números enteros aleatorios.
        
        '''
        return self.__rng.integers(minimo, maximo + 1, size=simulaciones)
    
    def graficar_frecuencia_enteros(self, minimo: int, maximo: int, simulaciones):
        ''' Genera números aleatorios enteros y grafica su frecuencia de aparición.

        Parámetros
        ----------
        minimo (int): Límite inferior del rango (incluido).
        maximo (int): Límite superior del rango (incluido).
        simulaciones (int): Número total de simulaciones a realizar.

        Retorna
        -------
        None
        
        '''
        datos = self.vector_enteros(minimo, maximo, simulaciones)
        valores, frecuencias = np.unique(datos, return_counts=True)

        plt.figure(figsize=(12, 6))
        plt.bar(valores, frecuencias, color='mediumseagreen', edgecolor='black')
        plt.title(f"Frecuencia de {simulaciones} números aleatorios en [{minimo}, {maximo}]")
        plt.xlabel("Número")
        plt.ylabel("Frecuencia")
        plt.xticks(np.arange(minimo, maximo + 1))
        plt.grid(axis='y', linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()

        
j = GeneradorAleatorio()
j.graficar_frecuencia_enteros(0, 36, 10)