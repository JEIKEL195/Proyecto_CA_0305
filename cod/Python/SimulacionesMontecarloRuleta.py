# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 05:58:46 2025

@author: jeike
"""

from JugadorRuleta import JugadorRuleta
from Ruleta import Ruleta
import numpy as np
import matplotlib.pyplot as plt

class SimulacionesMontecarloRuleta:
    def __init__(self, jugador: JugadorRuleta, ctd_simulaciones: int, ctd_jugadas: int):
        ''' Inicializa la simulación Montecarlo.

        Parámetros
        ----------
        jugador (JugadorRuleta): Instancia del jugador.
        tipo_apuesta (str): Tipo de apuesta ('numero', 'color', etc.).
        valor_apuesta: Valor de la apuesta.
        monto (float): Monto apostado por jugada.
        ctd_simulaciones (int): Cantidad total de simulaciones.
        ctd_jugadas (int): Cantidad de jugadas por simulación.
        
        '''
        self.__jugador_original = jugador
        self.__ctd_simulaciones = ctd_simulaciones
        self.__ctd_jugadas = ctd_jugadas
        self.__resultados = []

    def simular(self, tipo_apuesta: str, valor_apuesta, monto: float):
        for simulacion in range(self.__ctd_simulaciones):
            ruleta = Ruleta()
            jugador = JugadorRuleta(self.__jugador_original.nombre, self.__jugador_original.saldo)
            
            for _ in range(self.__ctd_jugadas):
                if(monto > jugador.saldo):
                    break  # no puede apostar más

                jugador.hacer_apuesta(tipo_apuesta, valor_apuesta, monto)
                resultado = ruleta.girar()
                jugador.actualizar_saldo(resultado)

            self.__resultados.append(jugador.saldo)
            
        return self.__resultados

    def estadisticas(self):
        ''' Retorna resumen estadístico de las simulaciones. '''
        return {
            'promedio_final': np.mean(self.__resultados),
            'desviacion_std': np.std(self.__resultados),
            'maximo': max(self.__resultados),
            'minimo': min(self.__resultados)
        }