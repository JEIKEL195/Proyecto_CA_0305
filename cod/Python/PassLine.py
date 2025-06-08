# -*- coding: utf-8 -*-
"""
Created on Sat Jun  7 02:20:44 2025

@author: Josué
"""

import matplotlib.pyplot as plt
from GeneradorAleatorio import GeneradorAleatorio as ga

class PassLine():
    '''
    Clase que modela la lógica de la apuesta Pass Line en el juego de Craps.
    Permite simular apuestas, lanzar dados, aplicar reglas del juego y graficar la evolución de la riqueza.
    '''
    
    def __init__(self):
        '''
        Inicializa los atributos necesarios para la apuesta Pass Line, incluyendo las sumas ganadoras, perdedoras,
        sumas que establecen punto, riqueza acumulada, número de apuestas y el valor del punto actual.

        Parámetros
        ----------
        None
        '''
        self.__sumas_ganadoras = [7, 11]
        self.__sumas_perdedoras = [2, 3, 12]
        self.__sumas_punto = [4, 5, 6, 8, 9, 10]
        self.__riqueza = []
        self.__numero_apuestas = 0
        self.__punto = 0
    
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
    
    @property
    def punto(self):
        '''
        Devuelve el valor actual del punto en juego.

        Parámetros
        ----------
        None

        Returns
        -------
        int
            Valor del punto.
        '''
        return self.__punto
    
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
    
    @punto.setter
    def punto(self, nuevo_punto):
        '''
        Asigna un nuevo valor al punto actual.

        Parámetros
        ----------
        nuevo_punto : int
            Valor del nuevo punto.
        '''
        self.__riqueza = nuevo_punto
    
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
        Devuelve una descripción textual de las reglas básicas de la apuesta Pass Line.

        Parámetros
        ----------
        None

        Returns
        -------
        str
            Explicación de las condiciones de victoria y derrota en el Come Out Roll y el punto.
        '''
        return f'Para ganar en el Come Out Roll, tu suma debe estar en: \n{self.__sumas_ganadoras} \nPara perder en el Come Out Roll, tu suma debe estar en: \n{self.__sumas_perdedoras} \nSi sacas otra suma, entras al punto: \nGanas si tu suma es igual a tu suma anterior y sale antes que el 7. \nSi sacas 7 primero pierdes'    
    
    def dinero_apuesta(self, dinero_apuesta):
        '''
        Agrega una cantidad de dinero inicial o apostada a la lista de riqueza.

        Parámetros
        ----------
        dinero_apuesta : float
            Valor de la apuesta inicial o monto a registrar.
        '''
        self.__riqueza.append(dinero_apuesta)
    
    
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
    
    def odds_pass(self, punto):
        '''
        Devuelve el factor de pago de una apuesta de odds, dependiendo del valor del punto.

        Parámetros
        ----------
        punto : int
            Valor del punto establecido.

        Returns
        -------
        float
            Multiplicador de ganancia para la apuesta de odds.
        '''
        match punto:
            
            case 4 | 10: 
                return 2
            
            case 5 | 9:
                return 1.5
            
            case 6 | 8:
                return 1.2
    
    def punto_pass_line(self, suma_dados_vieja, suma_dados_nueva):
        '''
        Determina si se gana o pierde durante la fase de punto del juego.

        Parámetros
        ----------
        suma_dados_vieja : int
            Suma que estableció el punto.
        suma_dados_nueva : int
            Nueva suma obtenida en el lanzamiento.

        Returns
        -------
        bool
            True si se ganó, False si se perdió o se sigue lanzando.
        '''
        if suma_dados_nueva == 7:
            return False
            
        elif suma_dados_vieja == suma_dados_nueva:
            return True
            
        else:
            self.__punto = suma_dados_vieja
            suma_dados = self.lanzar_dados()
            return self.punto_pass_line(self.__punto, suma_dados)
    
    def pass_line(self, porcentaje_apuesta, porcentaje_odds: float):
        '''
        Ejecuta una ronda de la apuesta Pass Line, aplicando lógica del Come Out Roll y del punto.

        Parámetros
        ----------
        porcentaje_apuesta : float
            Porcentaje del capital a apostar inicialmente.
        porcentaje_odds : float
            Porcentaje adicional apostado como odds.

        Returns
        -------
        str
            Resultado textual de la apuesta.
        '''
        self.__numero_apuestas = self.__numero_apuestas + 1
     
        suma_dados = self.lanzar_dados()

        if suma_dados in self.__sumas_ganadoras:
            self.__riqueza.append(self.__riqueza[self.__numero_apuestas -1]*(1 + porcentaje_apuesta))
            return 'Ganaste en el Come Out Roll'
        
        elif suma_dados in self.__sumas_perdedoras:
            self.__riqueza.append(self.__riqueza[self.__numero_apuestas-1]*(1 - porcentaje_apuesta))
            return 'Perdiste en el Come Out Roll'
        
        else:
            self.__punto = suma_dados
            nueva_suma = self.lanzar_dados()
                
            if self.punto_pass_line(self.__punto, nueva_suma) == True:
                self.__riqueza.append(self.__riqueza[self.__numero_apuestas-1]*(1 + porcentaje_apuesta + porcentaje_odds*self.odds_pass(self.__punto)))
                return 'Sacaste el punto, ganaste'
            else:
                self.__riqueza.append(self.__riqueza[self.__numero_apuestas-1]*(1 - porcentaje_apuesta - porcentaje_odds))
                return 'Sacaste 7 antes que el punto, perdiste'
                
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
    
    def capital_esperado(self, porcentaje_fijo, num_apuestas):
        '''
        Calcula el capital esperado al cabo de cierto número de apuestas, usando una aproximación con ventaja de la casa.

        Parámetros
        ----------
        porcentaje_fijo : float
            Porcentaje apostado en cada ronda.
        num_apuestas : int
            Número de rondas realizadas.

        Returns
        -------
        float
            Valor esperado del capital al final del proceso.
        '''
        return self.__riqueza[0] *( (1-porcentaje_fijo*0.0141)^(num_apuestas) )


apuesta1 = PassLine()
apuesta1.dinero_apuesta(1000)
apuesta1.pass_line(0.5, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)
apuesta1.pass_line(0.1, 0.3)



apuesta1.graficar_riqueza()
