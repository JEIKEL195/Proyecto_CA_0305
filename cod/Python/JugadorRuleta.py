# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 01:44:40 2025

@author: jeike
"""
from ApuestaRuleta import ApuestaRuleta

class JugadorRuleta:
    def __init__(self, nombre: str, saldo_inicial: float):
        '''Inicializa al jugador con un nombre y saldo disponible.

        Parámetros
        ----------
        nombre (str): Nombre del jugador.
        saldo_inicial (float): Saldo inicial disponible.

        Retorna
        -------
        None
        
        '''
        self.__nombre = nombre
        self.__saldo = saldo_inicial
        self.__apuestas = []
        
        
    @property
    def nombre(self):
        ''' Obtiene el nombre del jugador.
    
        Parámetros
        ----------
        None
    
        Retorna
        -------
        (str): Nombre del jugador.
        
        '''
        return self.__nombre
    
    @property 
    def saldo(self):
        ''' Obtiene el saldo actual del jugador.

        Parámetros
        ----------
        None
    
        Retorna
        -------
        (float): Saldo actual del jugador.
        
        '''
        return self.__saldo
    
    @nombre.setter 
    def nombre(self, new_value: str):
        ''' Establece un nuevo nombre para el jugador.

        Parámetros
        ----------
        new_value (str): Nuevo nombre del jugador.
    
        Retorna
        -------
        None
        
        '''
        self.__nombre = new_value
        
    
    def hacer_apuesta(self, tipo: str, valor, monto: float):
        '''Crea una apuesta si el monto es válido.

        Parámetros
        ----------
        tipo (str): Tipo de apuesta ('numero', 'color', etc.).
        valor: Valor específico de la apuesta (ej. 17, 'rojo', 'par').
        monto (float): Dinero apostado.

        Retorna
        -------
        Apuesta (ApuestaRuleta): Objeto de tipo Apuesta si válida, o None.
        
        '''
        if (monto <= 0):
            return None
        
        if (monto > self.__saldo):
            return None

        apuesta = ApuestaRuleta(tipo, valor, monto)
        
        self.__saldo -= monto
        self.__apuestas.append(apuesta)
        
        return apuesta

    def actualizar_saldo(self, resultado_ruleta):
        '''Actualiza el saldo en función del resultado de la ruleta.

        Parámetros
        ----------
        resultado_ruleta (tuple): Resultado del giro de la ruleta (número, color, paridad).

        Retorna
        -------
        float: Ganancia neta (puede ser negativa).
        '''
        ganancia_total = 0
        for apuesta in self.__apuestas:
            resultado = apuesta.calcular_pago_total(resultado_ruleta)
            self.__saldo += resultado
            ganancia_total += resultado
        self.__apuestas = []  # limpia apuestas después del giro
        return ganancia_total
