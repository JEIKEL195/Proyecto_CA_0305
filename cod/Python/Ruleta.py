# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 22:42:42 2025

@author: Jeikel Navarro Solis
"""

import numpy as np

class Ruleta:
    def __init__(self):
        
        self.__numeros = list(range(37))


    def girar(self):
        
        resultado = np.random.default_rng().choice(self.__numeros)
        color = self.color(resultado)
        paridad = self.paridad(resultado)
        
        return resultado, color, paridad
    
    
    def color(self, valor: int):
        rojo = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36],
        negro = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
        
        if valor in rojo:
            return 'rojo'
        
        elif valor in negro:
            return 'negro'
        
        else:
            return 'verde'


    def paridad(self, valor: int):
        
        if valor == 0:
            return 'ninguno'
        
        elif (valor % 2) == 0:
            return 'par'
        
        else:
            return 'impar'