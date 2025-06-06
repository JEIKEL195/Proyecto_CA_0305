# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 00:57:28 2025

@authors: Jeikel Navarro; Cristhofer Urrutia; Erick Venagas 
"""

from GeneradorAleatorio import GeneradorAleatorio as ga

class Craps:
    
    def __init__(self):
        
        self.__sumas_ganadoras = [7, 11]
        self.__sumas_perdedoras = [2, 3, 12]
        self.__sumas_punto = [4, 5, 6, 8, 9, 10]
    
    # Faltan gets y str donde se especifiquen cuanto gana si sale tal número.
    
    def punto_pass_line(self, suma_dados_vieja, suma_dados_nueva):
        
        if suma_dados_nueva == 7:
            return False
        
        elif suma_dados_vieja == suma_dados_nueva:
            return True
        
        else:
            dados = ga()
            dado1 = dados.entero(1, 6)
            dado2 = dados.entero(1, 6)
            suma_dados = dado1 + dado2
            
            return self.punto_pass_line(suma_dados_nueva, suma_dados)
            
    
    def pass_line(self):
        
        dados = ga()
        dado1 = dados.entero(1, 6)
        dado2 = dados.entero(1, 6)
        
        suma_dados = dado1 + dado2
        print(suma_dados)
    
        if suma_dados in self.__sumas_ganadoras:
            
            return 'Ganaste'
        
        elif suma_dados in self.__sumas_perdedoras:
            
            return 'Perdiste'
        
        else:
            
            dado1_nuevo = dados.entero(1, 6)
            dado_2nuevo = dados.entero(1,6)
            nueva_suma = dado1_nuevo + dado_2nuevo
            
            if self.punto_pass_line(suma_dados, nueva_suma) == True:
                return 'Ganaste :D'
            else:
                return 'Perdiste D:'
            
    
    
    def punto_dont_pass_line(self, suma_dados_vieja, suma_dados_nueva):
        
        if suma_dados_nueva == 7:
            return True
        
        elif suma_dados_nueva == suma_dados_vieja:
            return False
        
        else: 
            
            dados = ga()
            dado1 = dados.entero(1, 6)
            dado2 = dados.entero(1, 6)
            suma_dados = dado1 + dado2
            return self.punto_dont_pass_line(suma_dados_nueva, suma_dados)
        
            
    def dont_pass_line(self):
        
        suma_perdedora = [7,11]
        suma_ganadora = [2, 3]
        suma_empate = 12
        
        dados = ga()
        dado1 = dados.entero(1, 6)
        dado2 = dados.entero(1, 6)
        suma_dados = dado1 + dado2
        
        if suma_dados in suma_perdedora:
            return 'Perdiste'
        
        elif suma_dados in suma_ganadora:
            return 'Ganaste'
        
        elif suma_dados == suma_empate:
            return 'Empataste'
        
        else: 
            
            dado1_nuevo = dados.entero(1, 6)
            dado_2nuevo = dados.entero(1, 6)
            nueva_suma = dado1_nuevo + dado_2nuevo
            
            if self.punto_dont_pass_line(suma_dados, nueva_suma) == False:
                return 'Perdiste D:'
            
            else:
                return 'Ganaste :D'
            
            
        
            
                

        
apuesta = Craps()
apuesta.dont_pass_line()


