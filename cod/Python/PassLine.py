# -*- coding: utf-8 -*-
"""
Created on Sat Jun  7 02:20:44 2025

@author: Josué
"""

import matplotlib.pyplot as plt
from GeneradorAleatorio import GeneradorAleatorio as ga

class PassLine():
    
    
    def __init__(self):
        
        self.__sumas_ganadoras = [7, 11]
        self.__sumas_perdedoras = [2, 3, 12]
        self.__sumas_punto = [4, 5, 6, 8, 9, 10]
        self.__riqueza = []
        self.__numero_apuestas = 0
        self.__punto = 0
    
    @property
    def riqueza(self):
        return self.__riqueza
    
    @property
    def numero_apuestas(self):
        return self.__numero_apuestas
   
    @property
    def sumas_ganadoras(self):
        return self.__sumas_ganadoras
    
    @property
    def sumas_perdedoras(self):
        return self.__sumas_perdedoras
    
    @property
    def sumas_punto(self):
        return self.__sumas_punto
    
    @property
    def punto(self):
        return self.__punto
    
    @sumas_ganadoras.setter
    def sumas_ganadoras(self, nuevas_sumas_ganadoras):
        self.__sumas_ganadoras = nuevas_sumas_ganadoras
    
    @sumas_perdedoras.setter
    def sumas_perdedoras(self, nuevas_sumas_perdedoras):
        self.__sumas_perdedoras = nuevas_sumas_perdedoras
    
    @sumas_punto.setter
    def sumas_punto(self, nuevas_sumas_punto):
        self.__sumas_punto = nuevas_sumas_punto
    
    @riqueza.setter
    def riqueza(self, nueva_riqueza):
        self.__riqueza = nueva_riqueza
    
    @numero_apuestas.setter
    def numero_apuestas(self, nuevo_numero_apuestas):
        self.__numero_apuestas = nuevo_numero_apuestas
    
    def __str__(self):
        return f'Para ganar en el Come Out Roll, tu suma debe estar en: \n{self.__sumas_ganadoras} \nPara perder en el Come Out Roll, tu suma debe estar en: \n{self.__sumas_perdedoras} \nSi sacas otra suma, entras al punto: \nGanas si tu suma es igual a tu suma anterior y sale antes que el 7. \nSi sacas 7 primero pierdes'    
    
    def dinero_apuesta(self, dinero_apuesta):
        self.__riqueza.append(dinero_apuesta)
    
    
    def lanzar_dados(self):
        
        dados = ga()
        dado1 = dados.entero(1, 6)
        dado2 = dados.entero(1, 6)
        
        return dado1 + dado2
    
    def odds_pass(self, punto):
        
        match punto:
            
            case 4 | 10: 
                return 2
            
            case 5 | 9:
                return 1.5
            
            case 6 | 8:
                return 1.2
    
    def punto_pass_line(self, suma_dados_vieja, suma_dados_nueva):
        
        
        if suma_dados_nueva == 7:
            return False
            
        elif suma_dados_vieja == suma_dados_nueva:
            return True
            
        else:
            
            self.__punto = suma_dados_vieja
            suma_dados = self.lanzar_dados()
            return self.punto_pass_line(self.__punto, suma_dados)
            
    
    def pass_line(self, porcentaje_apuesta, porcentaje_odds: float):
        
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
        
        return self.__dinero_apuesta *( (1-porcentaje_fijo*0.0141)^(num_apuestas) )
    
    
    
apuesta1 = PassLine()
apuesta1.dinero_apuesta(1000)
apuesta1.pass_line(0.1, 0)
apuesta1.pass_line(0.1, 0)
apuesta1.pass_line(0.1, 0)
apuesta1.pass_line(0.1, 0)
apuesta1.pass_line(0.1, 0)
apuesta1.pass_line(0.1, 0)
apuesta1.pass_line(0.1, 0)
apuesta1.pass_line(0.1, 0)
apuesta1.pass_line(0.1, 0)
apuesta1.pass_line(0.1, 0)
apuesta1.pass_line(0.1, 0)
apuesta1.pass_line(0.1, 0)
apuesta1.pass_line(0.1, 0)
apuesta1.pass_line(0.1, 0)
apuesta1.pass_line(0.1, 0)
apuesta1.pass_line(0.1, 0)
apuesta1.pass_line(0.1, 0)
apuesta1.pass_line(0.1, 0)
apuesta1.pass_line(0.1, 0)
apuesta1.pass_line(0.1, 0)
apuesta1.pass_line(0.1, 0)
apuesta1.pass_line(0.1, 0)
apuesta1.pass_line(0.1, 0)
apuesta1.pass_line(0.1, 0)






apuesta1.graficar_riqueza()
