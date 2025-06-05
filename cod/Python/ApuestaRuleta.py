# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 23:17:05 2025

@author: Jeikel Navarro Solis
"""

class Apuesta:
    def __init__(self, tipo, valor, monto):
        
        self.__tipo = tipo
        self.__valor = valor
        self.__monto = monto

    def calcular_pago(self, resultado):
        numero, color, paridad = resultado

        if (self.__tipo == 'numero') and (self.__valor == numero):
            return self.__monto * 35
        
        elif (self.__tipo == 'color') and (self.__valor == color):
            return self.__monto * 1
        
        elif (self.__tipo == 'paridad') and (self.__valor == paridad):
            return self.monto * 1
        
        elif (self.__tipo == 'alto_bajo'):
            
            if (numero == 0):
                return 0
            
            parte = 'bajo' if 0 < numero < 19 else 'alto'
            
            if (self.__valor == parte):
                return self.__monto * 1
            
        elif (self.__tipo == 'docena'):
            
            if (numero == 0):
                return 0
            
            if ((self.__valor == 1) and (1 <= numero <= 12)):
                return self.monto * 2
            
            elif ((self.__valor == 2) and (13 <= numero <= 24)):
                return self.monto * 2
            
            elif ((self.__valor == 3) and (25 <= numero <= 36)):
                return self.__monto * 2
            
        elif (self.__tipo == 'columna'):
            
            if (numero == 0):
                return 0
            
            col = ((numero - 1) % 3) + 1
            
            if (self.__valor == col):
                return self.__monto * 2
            
        return 0
    
    
    def calcular_pago_total(self, resultado):
        pago = self.calcular_pago(resultado)
        
        if (pago > 0):
            return self.__monto + pago
        
        else:
            return -self.__monto
