# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 23:17:05 2025

@authors: Jeikel Navarro; Cristofer Urrutia; Erick Venegas
"""

import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class BlackjackSimulador:
    """
    Clase para simular el juego de BlackJack, la clase no tiene intención de ser interactiva.
    Sirve para el análisis de las estrategias más comunes. Analiza el rendimiento según el monto inicial y la estrategia.
    """
    def __init__(self, estrategia, monto_inicial, repeticiones = 100):
        self.__estrategia = estrategia.lower()
        self.__monto_inicial = monto_inicial
        self.__repeticiones = repeticiones
        self.__cartas = [2,3,4,5,6,7,8,9,10]*16 + ['J','Q','K','A']*16

    # Métodos Get.
    @property
    def estrategia(self):
        return self.__estrategia

    @property
    def monto_inicial(self):
        return self.__monto_inicial

    @property
    def repeticiones(self):
        return self.__repeticiones

    @property
    def cartas(self):
        return self.__cartas.copy()

    # Métodos set.
    @estrategia.setter
    def estrategia(self, nueva_estrategia):
        self.__estrategia = nueva_estrategia.lower()

    @monto_inicial.setter
    def monto_inicial(self, nuevo_monto):
        if nuevo_monto >= 0:
            self.__monto_inicial = nuevo_monto
        else:
            raise ValueError('El monto inicial debe ser mayor o igual a 0.')

    @repeticiones.setter
    def repeticiones(self, nuevas_reps):
        if nuevas_reps > 0:
            self.__repeticiones = nuevas_reps
        else:
            raise ValueError('El número de repeticiones debe ser mayor a 0.')

    # Método str.
    def __str__(self):
        return (f"Simulador de Blackjack\n"
                f"Estrategia: {self.estrategia.title()}\n"
                f"Monto inicial: {self.monto_inicial}\n"
                f"Repeticiones: {self.repeticiones}")

    def _valor_carta(self, carta):
        """
        Método que permite obtener el valor número de una carta.

        Parámetros:
        -----------
        carta (str): Carta con denominación a interpretar.

        Retorna:
        --------
        carta (int): Retorna el valor de la carta en forma numérica.
        """
        if carta in ['J', 'Q', 'K']:
            return 10
        elif carta == 'A':
            return 11
        return carta

    def _total(self, mano):
        """
        Método que permite obtener el total de un mazo, es decir, la suma del total de cartas.

        Parámetros:
        -----------
        mano (list): lista con las cartas.

        Retorna:
        --------
        total (int): Retorna el valor numérico de la suma de las denominaciones.
        """
        total = 0
        ases = 0
        for carta in mano:
            if isinstance(carta, int):
                total += carta
            elif carta in ['J', 'Q', 'K']:
                total += 10
            else:
                ases += 1
        for _ in range(ases):
            total += 11 if total + 11 <= 21 else 1
        return total

    def _repartir_carta(self, mano, mazo):
        """
        Método que permite obtener una carta de forma aleatoria.
        No retorna ningún valor, su función es cambiar la naturaleza de las manos de los jugadores.

        Parámetros:
        -----------
        mano (list): Lista con las cartas del jugador o dealer.
        mazo (list): Mazo con las cartas disponibles para ser jugadas.

        Retorna:
        --------
        None: El método no tiene retorno, cambia la naturaleza de las manos jugadas
        """
        carta = random.choice(mazo)
        mano.append(carta)
        mazo.remove(carta)

    def jugar(self):
        """
        Método que permite simular el juego de BLackjack.
        No tiene ningún retorno, su utilidad radica en mantener el juego hasta que el jugador se quede sin dinero.

        Parámetros:
        -----------
        None: No recibe parámetros.

        Retorna:
        --------
        None: No retorna ningún parámetro.
        """
        balance = self.monto_inicial
        turnos = 0 # Cantidad de turnos a imprimir.

        while balance > 0:
            turnos += 1
            apuesta = 1
            if apuesta > balance:
                break
            balance -= apuesta

            mazo = self.cartas.copy()
            mano_jugador = []
            mano_dealer = []
            for _ in range(2):
                self._repartir_carta(mano_dealer, mazo)
                self._repartir_carta(mano_jugador, mazo)

            # Aplicar estrategia
            if self.estrategia == 'quedarse':
                pass
            elif self.estrategia == 'como casa':
                while self._total(mano_jugador) <= 16:
                    self._repartir_carta(mano_jugador, mazo)
            elif self.estrategia == 'siempre doblar':
                if balance >= apuesta:
                    balance -= apuesta
                    apuesta *= 2
                    self._repartir_carta(mano_jugador, mazo)
            elif self.estrategia == 'quedarse y tomar seguro':
                if mano_dealer[0] == 'A' and balance >= 0.5:
                    balance -= 0.5  # costo del seguro
            elif self.estrategia == 'siempre split':
                if len(mano_jugador) == 2 and self._valor_carta(mano_jugador[0]) == self._valor_carta(mano_jugador[1]) and balance >= apuesta:
                    balance -= apuesta
                    manos = [[mano_jugador[0]], [mano_jugador[1]]]
                    for mano in manos:
                        self._repartir_carta(mano, mazo)
                        while self._total(mano) <= 16:
                            self._repartir_carta(mano, mazo)
                    mano_jugador = random.choice(manos)

            # Juego del dealer
            while self._total(mano_dealer) <= 16:
                self._repartir_carta(mano_dealer, mazo)

            total_jugador = self._total(mano_jugador)
            total_dealer = self._total(mano_dealer)

            if total_jugador > 21:
                pass  # pierde
            elif total_dealer > 21 or total_jugador > total_dealer:
                balance += 2 * apuesta
            elif total_jugador == total_dealer:
                balance += apuesta

        return turnos

    def simular(self, montos):
        """
        Método que permite realizar las simulaciones del juego.

        Parámetros:
        -----------
        montos (list): Recibe una lista de montos a evaluar para analizar el número de jugadas a diferentes montos.

        Retorna:
        --------
        resultados (dict): Retorna un diccionario, en donde cada clave es el monto inicial y el valor es una lista con el número de juagdas realizadas.
        """
        resultados = {}
        for monto in montos:
            self.monto_inicial = monto
            jugadas = [self.jugar() for _ in range(self.repeticiones)]
            resultados[monto] = jugadas
        return resultados

    def graficar(self, resultados):
        """
        Método que permite graficar el promedio de jugadas más el error estándar.

        Parámetros:
        -----------
        resultados (dict): Recibe un diccionario, para graficar el número de jugadas según el monto incial.

        Retorna:
        --------
        None: El método no retorna ningún valor, solo imprime el gráfico.
        """
        promedios = [np.mean(resultados[m]) for m in resultados]
        desviaciones = [np.std(resultados[m]) for m in resultados]

        plt.errorbar(list(resultados.keys()), promedios, yerr=desviaciones, fmt = '-o', capsize = 5)
        plt.xlabel('Monto inicial')
        plt.ylabel('Jugadas hasta perder (promedio ± std)')
        plt.title(f"Simulación Blackjack - Estrategia: {self.estrategia.title()} ({self.repeticiones} simulaciones)")
        plt.grid(True)
        plt.show()

    def histograma(self, resultados, monto):
        """
        Método que permite graficar la distribución de jugadas, es decir, la frecuencia de cada número de jugadas.

        Parámetros:
        -----------
        resultados (dict): Recibe un diccionario, para graficar el número de jugadas según el monto incial.
        monto (int): Recibe el monto para evaluar el número de jugadas.

        Retorna:
        --------
        None: El método no retorna ningún valor, solo imprime el gráfico.
        """
        plt.hist(resultados[monto], bins = 30, color = 'orchid', edgecolor = 'black')
        plt.title(f"Distribución de jugadas hasta perder - Estrategia: {self.estrategia.title()} (Monto: {monto})")
        plt.xlabel('Jugadas hasta perder')
        plt.ylabel('Frecuencia')
        plt.grid(True)
        plt.show()

    def boxplot(self, resultados):
        """
        Método que permite visualizar el valor promedio de jugadas que se pueden realizar según cada monto inicial.

        Parámetros:
        -----------
        resultados (dict): Recibe un diccionario, para graficar el número de jugadas según el monto inicial.

        Retorna:
        --------
        None: El método no retorna ningún valor, solo imprime el gráfico.
        """
        data = [{'Monto': m, 'Jugadas': j} for m in resultados for j in resultados[m]]
        df = pd.DataFrame(data)
        sns.boxplot(x = 'Monto', y = 'Jugadas', data = df, color = 'salmon')
        plt.title(f"Boxplot de jugadas según monto inicial\nEstrategia: {self.estrategia.title()}")
        plt.grid(True)
        plt.show()

    def probabilidad_sobrevivencia(self, resultados, rondas):
        """
        Método que permite calcular la probabilidad de sobrevivir a un número de rondas establecido.

        Parámetros:
        -----------
        resultados (dict): Recibe un diccionario, para graficar el número de jugadas según el monto inicial.
        rondas (int): Número de jugadas para evaluar la probabilidad de que la estrategia aguante hasta dicha ronda.

        Retorna:
        --------
        probs (dict): Retorna un diccionario, en donde la clave es el monto inicial y el valor es la probabilidad asociada.
        """
        probs = {}
        for monto in resultados:
            jugadas = np.array(resultados[monto])
            probs[monto] = np.mean(jugadas > rondas)
        return probs

    def graficar_probabilidad_sobrevivencia(self, resultados, rondas):
        """
        Método que permite graficar la probabilidad de sobreviviencia según el monto inicial.

        Parámetros:
        -----------
        resultados (dict): Recibe un diccionario, para graficar el número de jugadas según el monto inicial.
        rondas (int): Número de jugadas para evaluar la probabilidad de que la estrategia aguante hasta dicha ronda.

        Retorna:
        --------
        None: EL método no retorna ningún valor, solo imprime el respectivo gráfico.
        """
        probs = self.probabilidad_sobrevivencia(resultados, rondas)
        plt.plot(list(probs.keys()), list(probs.values()), marker = 'o', color = 'green')
        plt.xlabel('Monto inicial')
        plt.ylabel(f'Probabilidad de sobrevivir más de {rondas} jugadas')
        plt.title(f"Probabilidad de sobrevivencia ({self.estrategia.title()})")
        plt.grid(True)
        plt.show()