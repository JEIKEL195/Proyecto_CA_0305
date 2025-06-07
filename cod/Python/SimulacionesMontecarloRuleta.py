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
        self.__historiales = []

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
                
            self.__historiales.append(jugador.get_historial())    
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
    
    def simular_varias_apuestas(self, apuestas: list, num_jugadas: int):
        ''' Ejecuta una simulación con distintas apuestas.

        '''
        monto_total = sum(monto for _, _, monto in apuestas)
        
        for simulacion in range(self.__ctd_simulaciones):
            ruleta = Ruleta()
            jugador = JugadorRuleta(self.__jugador_original.nombre, self.__jugador_original.saldo)
            
            for _ in range(self.__ctd_jugadas):
                if(monto_total > jugador.saldo):
                    break  # no puede apostar más
        
                for tipo, valor, monto in apuestas:
                    jugador.hacer_apuesta(tipo, valor, monto)
        
                resultado = ruleta.girar()
                jugador.actualizar_saldo(resultado)
    
            self.__historiales.append(jugador.get_historial())
            self.__resultados.append(jugador.saldo)
        
        return self.__resultados
    
    def simular_martingala(self, tipo_apuesta, valor_apuesta, monto_inicial):
        for simulacion in range(self.__ctd_simulaciones):
            ruleta = Ruleta()
            jugador = JugadorRuleta(self.__jugador_original.nombre, self.__jugador_original.saldo)
            monto = monto_inicial
    
            for _ in range(self.__ctd_jugadas):
                if monto > jugador.saldo:
                    break
    
                jugador.hacer_apuesta(tipo_apuesta, valor_apuesta, monto)
                resultado = ruleta.girar()
                ganador = jugador.actualizar_saldo(resultado)
    
                if ganador:
                    monto = monto_inicial
                    
                else:
                    monto *= 2
                    
            self.__historiales.append(jugador.get_historial())
            self.__resultados.append(jugador.saldo)
            
        return self.__resultados
    
    def martingala_hasta_objetivo(self, tipo_apuesta: str, valor_apuesta, monto_inicial: float, factor_objetivo: float):
        '''Simula la estrategia Martingala hasta alcanzar el objetivo de capital o quedar sin saldo.'''
    
        saldo_objetivo = self.__jugador_original.saldo * factor_objetivo
        historial_tiempo = []
        exitos = 0  # contar cuántas veces se alcanza el objetivo
    
        for simulacion in range(self.__ctd_simulaciones):
            ruleta = Ruleta()
            jugador = JugadorRuleta(self.__jugador_original.nombre, self.__jugador_original.saldo)
            monto = monto_inicial
            historial = [jugador.saldo]
            tiempo = 0
    
            while 0 < jugador.saldo < saldo_objetivo:
                if monto > jugador.saldo:
                    break  # no puede apostar más
    
                jugador.hacer_apuesta(tipo_apuesta, valor_apuesta, monto)
                resultado = ruleta.girar()
                fue_ganador = jugador.actualizar_saldo(resultado)
                historial.append(jugador.saldo)
    
                if fue_ganador:
                    monto = monto_inicial
                else:
                    monto *= 2
                    
                tiempo += 1
    
            if jugador.saldo >= saldo_objetivo:
                exitos += 1
    
            self.__historiales.append(historial)
            self.__resultados.append(jugador.saldo)
            historial_tiempo.append(tiempo)
    
        probabilidad_exito = exitos / self.__ctd_simulaciones
        
        tiempo_promedio = sum(historial_tiempo)/self.__ctd_simulaciones
        
        return {
            'Éxitos': exitos,
            'Fracaso': self.__ctd_simulaciones - exitos,
            'Probabilidad_exito': probabilidad_exito,
            'Tiempo_promedio': tiempo_promedio
        }

    

    
    def trayectorias(self):
        ''' Grafica distintas trayectorias del juego de ruleta.

        Retorna
        -------
        None 
        
        '''
        for trayectoria in self.__historiales:
            x = list(range(len(trayectoria)))
            #plt.scatter(x, trayectoria, s=3)
            plt.plot(x, trayectoria, linewidth=1)
    
        plt.title(f'Trayectorias del saldo del jugador: {self.__jugador_original.nombre}')
        plt.xlabel('Número de jugadas')
        plt.ylabel('Saldo')
        plt.grid(True)
        plt.show()
    
    def graficar_probabilidad(self, factor_objetivo: float, particiones: list):
        '''Grafica la evolución de la probabilidad de terminar con el capital por un factor objetivo según distintas particiones.'''
    
        total_sim = len(self.__resultados)
        pasos = [particion for particion in particiones if particion <= total_sim]
    
        probabilidades = []
    
        for particion in pasos:
            subconjunto = self.__resultados[:particion]
            cantidad = [1 if dato >= factor_objetivo * self.__jugador_original.saldo else 0 for dato in subconjunto]
            probabilidad = sum(cantidad) / len(cantidad)
            probabilidades.append(probabilidad)
    
        plt.figure(figsize=(8, 5))
        plt.bar([str(paso) for paso in pasos], probabilidades, color='darkblue')
        plt.ylim(0, 1)
        plt.title(f'Probabilidad de terminar con {factor_objetivo} veces el capital según número de simulaciones')
        plt.xlabel('Cantidad de simulaciones consideradas')
        plt.ylabel(f'Probabilidad de terminar con {factor_objetivo} veces el capital')
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()
    
jugador = JugadorRuleta(nombre = "Venegas", saldo_inicial = 100)
sim = SimulacionesMontecarloRuleta(jugador, 10000, 5000)
#sim.simular_martingala('paridad', 'par', 1000)
#sim.simular_martingala_hasta_objetivo('paridad', 'par', 10, 2)
sim.martingala_inversa_hasta_objetivo('paridad', 'par', 10, 1.1)
#sim.graficar_probabilidad(2, [10, 100, 1000, 10_000])
#sim.estadisticas()
#sim.trayectorias()