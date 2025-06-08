# -*- coding: utf-8 -*-
"""
Created on Sat Jun  7 22:12:55 2025

@author: Admin
"""

from BlackJackSimuladoQuedarse import jugar_blackjack_simulado_quedarse
from BlackJackSimuladoQuedarseSeguro import jugar_blackjack_quedarse_seguro
from BlackJackSimuladoCasa import jugar_blackjack_como_casa
from BlackJackSimuladoDoblar import jugar_blackjack_doblando
import time
import numpy as np
import matplotlib.pyplot as plt

inicio = time.time()

# Lista de montos iniciales
montos = list(range(10, 110, 10))  # [10, 20, ..., 100]
num_simulaciones = 100

# Guardar promedios de jugadas
promedios_seguro = []
promedios_sin_seguro = []
promedios_casa = []
promedios_doblando = []

for monto in montos:
    # Simulaciones para la estrategia con seguro
    jugadas_seguro = [jugar_blackjack_quedarse_seguro(monto) for _ in range(num_simulaciones)]
    promedio_seguro = np.mean(jugadas_seguro)
    promedios_seguro.append(promedio_seguro)
    
    # Simulaciones para la estrategia sin seguro
    jugadas_sin_seguro = [jugar_blackjack_simulado_quedarse(monto) for _ in range(num_simulaciones)]
    promedio_sin_seguro = np.mean(jugadas_sin_seguro)
    promedios_sin_seguro.append(promedio_sin_seguro)

    # Simulaciones para la estrategia de la casa
    jugadas_casa = [jugar_blackjack_como_casa(monto) for _ in range(num_simulaciones)]
    promedio_casa = np.mean(jugadas_casa)
    promedios_casa.append(promedio_casa)

    # Simulaciones para la estrategia doblando
    jugadas_doblando = [jugar_blackjack_doblando(monto) for _ in range(num_simulaciones)]
    promedio_doblando = np.mean(jugadas_doblando)
    promedios_doblando.append(promedio_doblando)

# Graficar los promedios
plt.plot(montos, promedios_seguro, marker='o', linestyle='-', color='crimson', label='Con seguro')
plt.plot(montos, promedios_sin_seguro, marker='s', linestyle='--', color='blue', label='Sin seguro')
plt.plot(montos, promedios_casa, marker='^', linestyle='-.', color='green', label='Como la casa')
plt.plot(montos, promedios_doblando, marker='d', linestyle=':', color='purple', label='Doblado')

plt.xlabel('Monto inicial')
plt.ylabel('Promedio de turnos hasta perder')
plt.title('Comparación de Estrategias en Blackjack\n(100 simulaciones por monto)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

fin = time.time()
print(f"Tiempo de ejecución: {fin - inicio:.2f} segundos")