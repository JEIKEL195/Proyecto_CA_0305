# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 00:57:28 2025

@authors: Jeikel Navarro; Cristhofer Urrutia; Erick Venagas 
"""

import matplotlib.pyplot as plt

from GeneradorAleatorio import GeneradorAleatorio as ga

class Craps:
    
    def __init__(self):
        
        self.__sumas_ganadoras = [7, 11]
        self.__sumas_perdedoras = [2, 3, 12]
        self.__sumas_punto = [4, 5, 6, 8, 9, 10]
        self.__riqueza = []
        self.__numero_apuestas = 0
    
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
    
    @numero_apuestas
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
            
            suma_dados = self.lanzar_dados()
            return self.punto_pass_line(suma_dados_nueva, suma_dados)
            
    
    def pass_line(self, porcentaje_apuesta):
        
        self.__numero_apuestas = self.__numero_apuestas + 1
     
        suma_dados = self.lanzar_dados()
    
        if suma_dados in self.__sumas_ganadoras:
            
            self.__riqueza.append(self.__riqueza[self.__numero_apuestas -1]*(1 + porcentaje_apuesta))
            
            return 'Ganaste en el Come Out Roll'
        
        elif suma_dados in self.__sumas_perdedoras:
            
            self.__riqueza.append(self.__riqueza[self.__numero_apuestas-1]*(1 - porcentaje_apuesta))
            
            return 'Perdiste en el Come Out Roll'
        
        else:
            
            nueva_suma = self.lanzar_dados()
            
            if self.punto_pass_line(suma_dados, nueva_suma) == True:
                
                self.__riqueza.append(self.__riqueza[self.__numero_apuestas-1]*(1 + porcentaje_apuesta))
                
                return 'Sacaste el punto, ganaste'
            
            else:
                
                self.__riqueza.append(self.__riqueza[self.__numero_apuestas-1]*(1 - porcentaje_apuesta))
                
                return 'Sacaste 7 antes que el punto, perdiste'
            
    
    
    def punto_dont_pass_line(self, suma_dados_vieja, suma_dados_nueva):
        
        
        if suma_dados_nueva == 7:
            return True
        
        elif suma_dados_nueva == suma_dados_vieja:
            return False
        
        else: 
            
            suma_dados = self.lanzar_dados()
            return self.punto_dont_pass_line(suma_dados_nueva, suma_dados)
        
            
    def dont_pass_line(self, porcentaje_apuesta):
        
        self.__numero_apuestas = self.__numero_apuestas + 1
        
        suma_perdedora = self.__sumas_ganadoras
        suma_ganadora = [2, 3]
        suma_empate = 12
        
        suma_dados = self.lanzar_dados()
        
        if suma_dados in suma_perdedora:
            
            self.__riqueza.append(self.__riqueza[self.__numero_apuestas - 1]*(1 - porcentaje_apuesta))
            return 'Perdiste en el Come Out Roll'
        
        elif suma_dados in suma_ganadora:
            
            self.__riqueza.append(self.__riqueza[self.__numero_apuestas - 1]*(1 + porcentaje_apuesta))
            return 'Ganaste en el Come Out Roll'
        
        elif suma_dados == suma_empate:
            
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

# Etiquetas y título
        plt.xlabel('Número de apuestas')
        plt.ylabel('Riqueza')
        plt.title('Evolución de la Riqueza en el Tiempo')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    
    
apuesta1 = Craps()
apuesta1.dinero_apuesta(1000)
apuesta1.dont_pass_line(0.05)



apuesta1.graficar_riqueza()
