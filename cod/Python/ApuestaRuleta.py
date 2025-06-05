# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 23:17:05 2025

@authors: Jeikel Navarro; Cristofer Urrutia; Erick Venegas
"""

class ApuestaRuleta:
    def __init__(self, tipo, valor, monto):
        ''' Inicializa una apuesta con tipo, valor y monto.

        Parámetros
        ----------
        tipo (str): Tipo de apuesta ('numero', 'color', 'paridad', 'alto_bajo', 'docena', 'columna').
        valor: Valor apostado (puede ser número entero o cadena, dependiendo del tipo de apuesta).
        monto (float): Monto de dinero apostado.
        
        '''
        self.__tipo = tipo
        self.__valor = valor
        self.__monto = monto
        
    
    @property
    def tipo(self):
        ''' Obtiene el tipo de apuesta realizada.
    
        Parámetros
        ----------
        None
    
        Retorna
        -------
        (str): Tipo de apuesta ('numero', 'color', 'paridad', 'alto_bajo', 'docena', 'columna').
        
        '''
        return self.__tipo
        
    
    @property
    def valor(self):
        ''' Obtiene el valor asociado a la apuesta.
    
        Parámetros
        ----------
        None
    
        Retorna
        -------
        Valor específico de la apuesta (por ejemplo, un número, color, paridad, etc.).
        
        '''
        return self.__valor
    
    
    @property
    def monto(self):
        ''' Obtiene el monto de dinero apostado.
    
        Parámetros
        ----------
        None
    
        Retorna
        -------
        (float): Monto apostado.
        
        '''
        return self.__monto
    
    
    @tipo.setter
    def tipo(self, new_value: str):
        ''' Establece un nuevo tipo de apuesta.
    
        Parámetros
        ----------
        new_value (str): Nuevo tipo de apuesta.
    
        Retorna
        -------
        None
        
        '''
        self.__tipo = new_value
        
        
    @valor.setter
    def valor(self, new_value):
        ''' Establece un nuevo valor para la apuesta.
    
        Parámetros
        ----------
        new_value (int | str): Nuevo valor de la apuesta.
    
        Retorna
        -------
        None
        
        '''
        self.__valor = new_value
        
        
    @monto.setter
    def monto(self, new_value: float):
        ''' Establece un nuevo monto para la apuesta.
    
        Parámetros
        ----------
        new_value (float): Nuevo monto apostado.
    
        Retorna
        -------
        None
        
        '''
        self.__monto = new_value
        
        
    def __str__(self):
        ''' Representación en cadena de la apuesta.

        Parámetros
        ----------
        None

        Retorna
        -------
        (str): Descripción de la apuesta, incluyendo tipo, valor y monto.
        
        '''
        return f"Apuesta de tipo '{self.__tipo}' con valor '{self.__valor}' por un monto de {self.__monto}."

    def calcular_pago(self, resultado):
        ''' Calcula la ganancia de la apuesta con base en el resultado de la ruleta.
        
        Parámetros
        ----------
        resultado (tuple): Resultado de la ruleta como tupla (numero, color, paridad).
        
        Retorna
        -------
        pago (float): Ganancia neta obtenida de la apuesta (sin incluir el monto original). Si se pierde, retorna 0.
        
        '''
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
        ''' Calcula el resultado total de la apuesta, incluyendo el monto original si se gana, o 0 si se pierde.

        Parámetros
        ----------
        resultado (tuple): Resultado de la ruleta como tupla (numero, color, paridad).

        Retorna
        -------
        total (float): Monto total recibido (monto + ganancia) si gana, o 0 si pierde.
        
        '''
        pago = self.calcular_pago(resultado)
        
        if (pago > 0):
            pago_total = self.__monto + pago
            return pago_total
        
        else:
            return 0
