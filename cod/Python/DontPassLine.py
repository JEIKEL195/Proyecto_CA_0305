# -*- coding: utf-8 -*-
"""
Created on Sat Jun  7 18:08:24 2025

@author: Josué
"""

import matplotlib.pyplot as plt
from GeneradorAleatorio import GeneradorAleatorio as ga

class DontPassLine():
    '''
    Clase que modela la lógica de la apuesta Dont Pass Line en el juego de Craps.
    Permite simular apuestas, lanzar dados, aplicar reglas del juego y graficar la evolución de la riqueza.
    '''
    
    def __init__(self):
        '''
        Inicializa los atributos necesarios para la apuesta Dont Pass Line, incluyendo sumas ganadoras, perdedoras,
        suma de empate, sumas que establecen punto, riqueza acumulada y número de apuestas.

        Parámetros
        ----------
        None
        '''
        self.__sumas_ganadoras = [2, 3]
        self.__sumas_perdedoras = [7, 11]
        self.__suma_empate = 12
        self.__sumas_punto = [4, 5, 6, 8, 9, 10]
        self.__riqueza = []
        self.__numero_apuestas = 0
        
    @property
    def riqueza(self):
        '''
        Devuelve la lista de riqueza acumulada después de cada apuesta.

        Parámetros
        ----------
        None

        Returns
        -------
        list
            Lista de valores de riqueza.
        '''
        return self.__riqueza
    
    @property
    def numero_apuestas(self):
        '''
        Devuelve el número total de apuestas realizadas.

        Parámetros
        ----------
        None

        Returns
        -------
        int
            Número de apuestas realizadas.
        '''
        return self.__numero_apuestas
   
    @property
    def sumas_ganadoras(self):
        '''
        Devuelve las sumas que ganan en el Come Out Roll.

        Parámetros
        ----------
        None

        Returns
        -------
        list
            Lista de sumas ganadoras.
        '''
        return self.__sumas_ganadoras
    
    @property
    def sumas_perdedoras(self):
        '''
        Devuelve las sumas que pierden en el Come Out Roll.

        Parámetros
        ----------
        None

        Returns
        -------
        list
            Lista de sumas perdedoras.
        '''
        return self.__sumas_perdedoras
    
    @property
    def sumas_punto(self):
        '''
        Devuelve las sumas que establecen un punto en el Come Out Roll.

        Parámetros
        ----------
        None

        Returns
        -------
        list
            Lista de sumas que establecen punto.
        '''
        return self.__sumas_punto
    
    @sumas_ganadoras.setter
    def sumas_ganadoras(self, nuevas_sumas_ganadoras):
        '''
        Establece una nueva lista de sumas ganadoras.

        Parámetros
        ----------
        nuevas_sumas_ganadoras : list
            Lista de nuevas sumas ganadoras.
        '''
        self.__sumas_ganadoras = nuevas_sumas_ganadoras
    
    @sumas_perdedoras.setter
    def sumas_perdedoras(self, nuevas_sumas_perdedoras):
        '''
        Establece una nueva lista de sumas perdedoras.

        Parámetros
        ----------
        nuevas_sumas_perdedoras : list
            Lista de nuevas sumas perdedoras.
        '''
        self.__sumas_perdedoras = nuevas_sumas_perdedoras
    
    @sumas_punto.setter
    def sumas_punto(self, nuevas_sumas_punto):
        '''
        Establece una nueva lista de sumas que definen punto.

        Parámetros
        ----------
        nuevas_sumas_punto : list
            Lista de nuevas sumas punto.
        '''
        self.__sumas_punto = nuevas_sumas_punto
    
    @riqueza.setter
    def riqueza(self, nueva_riqueza):
        '''
        Asigna una nueva lista de riqueza acumulada.

        Parámetros
        ----------
        nueva_riqueza : list
            Lista de valores de riqueza.
        '''
        self.__riqueza = nueva_riqueza
    
    @numero_apuestas.setter
    def numero_apuestas(self, nuevo_numero_apuestas):
        '''
        Asigna un nuevo número de apuestas realizadas.

        Parámetros
        ----------
        nuevo_numero_apuestas : int
            Número actualizado de apuestas.
        '''
        self.__numero_apuestas = nuevo_numero_apuestas
    
    def __str__(self):
        '''
        Devuelve una descripción textual de las reglas básicas de la apuesta Dont Pass Line.

        Parámetros
        ----------
        None

        Returns
        -------
        str
            Explicación de las condiciones de victoria, derrota y empate en el Come Out Roll y el punto.
        '''
        return f'Para ganar en el Come Out Roll, tu suma debe estar en: \n{self.__sumas_ganadoras} \nPara perder en el Come Out Roll, tu suma debe estar en: \n{self.__sumas_perdedoras} \nEmpatas si tu suma es igual a {self.__suma_empate} \nSi sacas otra suma, entras al punto: \nGanas si tu suma es igual a 7 y sale antes que el punto. \nSi sacas el punto primero pierdes'    
    
    
    def lanzar_dados(self):
        '''
        Simula el lanzamiento de dos dados y devuelve su suma.

        Parámetros
        ----------
        None

        Returns
        -------
        int
            Suma de dos dados simulados.
        '''
        dados = ga()
        dado1 = dados.entero(1, 6)
        dado2 = dados.entero(1, 6)
        
        return dado1 + dado2
    
    def punto_dont_pass_line(self, suma_dados_vieja, suma_dados_nueva):
        '''
        Determina el resultado en la fase de punto para la apuesta Dont Pass Line.

        Parámetros
        ----------
        suma_dados_vieja : int
            Suma que estableció el punto.
        suma_dados_nueva : int
            Nueva suma obtenida en el lanzamiento.

        Returns
        -------
        bool
            True si gana (sale 7 primero), False si pierde (sale punto primero), o sigue evaluando.
        '''
        if suma_dados_nueva == 7:
            return True
        
        elif suma_dados_nueva == suma_dados_vieja:
            return False
        
        else: 
            suma_dados = self.lanzar_dados()
            return self.punto_dont_pass_line(suma_dados_nueva, suma_dados)
        
            
    def dont_pass_line(self, porcentaje_apuesta):
        '''
        Ejecuta una ronda de la apuesta Dont Pass Line, aplicando lógica del Come Out Roll y del punto.

        Parámetros
        ----------
        porcentaje_apuesta : float
            Porcentaje del capital apostado.

        Returns
        -------
        str
            Resultado textual de la apuesta.
        '''
        self.__numero_apuestas = self.__numero_apuestas + 1
        
        suma_dados = self.lanzar_dados()
        
        if suma_dados in self.__suma_perdedora:
            self.__riqueza.append(self.__riqueza[self.__numero_apuestas - 1]*(1 - porcentaje_apuesta))
            return 'Perdiste en el Come Out Roll'
        
        elif suma_dados in self.__suma_ganadora:
            self.__riqueza.append(self.__riqueza[self.__numero_apuestas - 1]*(1 + porcentaje_apuesta))
            return 'Ganaste en el Come Out Roll'
        
        elif suma_dados == self.__suma_empate:
            self.__riqueza.append(self.__riqueza[self.__numero_apuestas - 1])
            return 'Empataste en el Come Out Roll'
        
        else: 
            dado1_nuevo = self.lanzar_dados()
            dado_2nuevo = self.lanzar_dados()
            nueva_suma = dado1_nuevo + dado_2nuevo
            
            if self.punto_dont_pass_line(suma_dados, nueva_suma) == False:
                self.__riqueza.append(self.__riqueza[self.__numero_apuestas - 1]*(1 - porcentaje_apuesta))
                return 'Perdiste, sacaste el punto antes que el 7'
            
            else:
                self.__riqueza.append(self.__riqueza[self.__numero_apuestas - 1]*(1 + porcentaje_apuesta))
                return 'Ganaste'
            
            
    def graficar_riqueza(self):
        '''
        Grafica la evolución de la riqueza del jugador a lo largo de las apuestas.

        Parámetros
        ----------
        None
        '''
        apuestas = range(self.__numero_apuestas + 1)

        plt.plot(apuestas, self.__riqueza, linestyle=':', color='#C0392B', linewidth=1)

        for i in range(1, len(self.__riqueza)):
            color = 'green' if self.__riqueza[i] > self.__riqueza[i - 1] else 'red'
            plt.plot(apuestas[i], self.__riqueza[i], 
             marker='o', 
             markersize=3.5, 
             markerfacecolor=color, 
             markeredgecolor='black',
             markeredgewidth=1)

        plt.xlabel('Número de apuestas')
        plt.ylabel('Riqueza')
        plt.title('Evolución de la Riqueza en el Tiempo')
        plt.grid(True)
        plt.tight_layout()
        plt.show()



        
