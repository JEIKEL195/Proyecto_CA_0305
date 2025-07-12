# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 22:42:42 2025

@authors: Jeikel Navarro; Cristofer Urrutia; Erick Venegas
"""

from GeneradorAleatorio import GeneradorAleatorio

class Ruleta:
    def __init__(self):
        self.__resultado = -1
        self.__color = ''
        self.__paridad = ''
        self.__rng = GeneradorAleatorio()
        
        
    def girar(self):
        '''Simula un giro de la ruleta.

        Parámetros
        ----------
        None
        
        Retorna
        -------
        (tuple): Tupla con tres elementos: resultado, color y paridad
        
        '''
        self.__resultado = self.__rng.entero(0, 36)
        self.__color = self.color(self.__resultado)
        self.__paridad = self.paridad(self.__resultado)
        
        return self.__resultado, self.__color, self.__paridad
    
    
    def color(self, valor: int):
        '''Determina el color correspondiente a un número de la ruleta.

        Parámetros
        ----------
        valor (int): Número entre 0 y 36 cuyo color se desea conocer.
        
        Retorna
        -------
        (str): 'rojo', 'negro' o 'verde' según el número.
        
        '''
        rojo = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
        negro = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
        
        if valor in rojo:
            return 'rojo'
        
        elif valor in negro:
            return 'negro'
        
        else:
            return 'verde'


    def paridad(self, valor: int):
        '''Determina la paridad de un número de la ruleta.

        Parámetros
        ----------
        valor (int): Número entre 0 y 36 cuya paridad se desea conocer.
        
        Retorna
        -------
        (str): 'par' si el número es par, 'impar' si es impar, y 'ninguno' si es cero.
        
        '''
            
        if valor == 0:
            return 'ninguno'
        
        elif (valor % 2) == 0:
            return 'par'
        
        else:
            return 'impar'
    