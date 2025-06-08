# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 23:17:05 2025

@authors: Jeikel Navarro; Cristofer Urrutia; Erick Venegas
"""
import random  # Con la librería se van a mezclar las cartas.
import time 
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def jugar_blackjack_doblando(monto):
    # Inicializa el balance del jugador el monto proporcionado.
    balance = monto
    # print(f"Tu balance inicial es: ${balance}"), no es necesario printear.

    # Función para repartir cartas
    def dealCard(turn, deck):
        card = random.choice(deck)  # Elige una carta aleatoria del mazo
        turn.append(card)  # Añade la carta a la mano del jugador o dealer
        deck.remove(card)  # Elimina la carta del mazo para no repetir

    # Función para calcular el total de una mano
    def total(turn):
        total = 0  # Inicializa el total
        face = ['J', 'Q', 'K']  # Cartas que valen 10
        ases = 0  # Contador de ases (pueden valer 11 o 1)
        
        # Calcula el valor base de las cartas (sin contar ases)
        for card in turn:
            if isinstance(card, int):  # Si es número (2-10)
                total += card
            elif card in face:  # Si es J, Q o K
                total += 10
            else:  # Si es A
                ases += 1
                
        # Calcula el valor óptimo de los ases
        for _ in range(ases):
            total += 11 if total + 11 <= 21 else 1  # As vale 11 si no se pasa de 21, sino 1
        return total

    # Función para mostrar solo una carta del dealer (la otra oculta)
    def revealDealerHand(dealerHand):
        return dealerHand[0], 'X'  # Devuelve primera carta y 'X' para la oculta

    # Función auxiliar para determinar valor real de cartas (usada en split)
    def valor_real(carta):
        return 10 if carta in ['J', 'Q', 'K'] else 11 if carta == 'A' else carta

    contador_turnos = 0

    # Bucle principal del juego (mientras el jugador tenga dinero)
    while balance > 0:
        contador_turnos += 1
        # print('')
        # print('='*40)
        # print('')
        # print(f"\nTu balance actual es: ${balance}")

        
        bet = 1 # Definimos que el jugador siempre apuesta 2 de su capital, para que cuando haga seguro, este pague 1.
        # Pedir apuesta al jugador
        while True:
            try:
                # bet = 2 #int(input("¿Cuánto deseas apostar? (0 para salir): "))
                if bet == 0:  # Opción para salir del juego
                    # print("Gracias por jugar. ¡Hasta la próxima!")
                    return
                elif 0 < bet <= balance:
                    balance -= bet # La apuesta es válida y restamos la cantidad apostada a su balance. 
                    break
                else:  # Apuesta inválida (fuera de rango)
                    # print("Apuesta inválida.")
                    return contador_turnos # Si la apuesta ya no se puede hacer.
            except:  # Manejo de errores si no ingresa un número
                # print("Por favor ingresa un número válido.")
                pass # Nunca entramos a esto, entonces solo pasamos

        # Inicializar variables para la ronda
        dealerHand = []  # Mano del dealer
        # Crear mazo con 6 barajas (combinación de números y figuras)
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10]*16 + ['J', 'Q', 'K', 'A']*16
        playerHand = []  # Mano del jugador
        
        # Repartir 2 cartas a cada uno
        for _ in range(2): 
            dealCard(dealerHand, deck) # Reparte las cartas al dealer. (El dealer siempre reparte primero)
            dealCard(playerHand, deck) # Reparte las cartas al jugador.

        # No jugamos Seguro, porque se juega como casa.
        seguro_apuesta = 0
        if dealerHand[0] == 'A' and len(dealerHand) == 2:
            seguro_apuesta = 0  # La mitad de la apuesta inicial, en este caso 1.
            # print(f"\nEl dealer muestra un As. Puedes tomar un seguro de ${seguro_apuesta}")
            # print(f"Tu mano: {playerHand} ({total(playerHand)})")
            # print(f"Apuesta principal: ${bet} | Balance: ${balance}")
            
            while True:
                # Siempre vamos a tomar el seguro cuando se pueda.
                opcion = 'n' # input("¿Quieres tomar el seguro? (s/n): ").lower()
                # time.sleep(1)
                if opcion == 's':
                    if balance >= seguro_apuesta:
                        balance -= seguro_apuesta
                        # print(f"Seguro de ${seguro_apuesta} aceptado. Balance actual: ${balance}")
                        # print('El dealer está mirando la carta para revelar el seguro al final de la jugada...')
                        # time.sleep(1)
                        break
                    else:
                        # print("Fondos insuficientes para el seguro")
                        seguro_apuesta = 0  # Cancelar seguro por fondos insuficientes
                        break
                elif opcion == 'n': # Nunca se entra a esta opción.
                    seguro_apuesta = 0  # Se rechaza el seguro.
                    # print('Has decidido no tomar el seguro')
                    # print('El juego continua')
                    break
                else:
                    # print("Opción inválida. Por favor ingresa 's' o 'n'")
                    pass

        # Listas para manejar splits (dividir)
        hands = [playerHand]  # Todas las manos del jugador (puede ser más de una si es split)
        apuestas = [bet]  # Apuestas correspondientes a cada mano
        resultados = []  # Para almacenar resultados de cada mano

        # Verificar si puede hacer split (dos cartas iguales y balance suficiente)
        puede_split = len(playerHand) == 2 and valor_real(playerHand[0]) == valor_real(playerHand[1]) and balance >= bet
        if puede_split:
            eleccion = 'n' # No vamos a Splitear aún. input(f"Tienes {playerHand}. ¿Deseas dividir (s/n)? ").lower()
            # time.sleep(1)
            if eleccion == 's':  # Si elige dividir
                # print('Has decidido dividir, por lo que ahora tienes dos manos y se tan dos cartas adicionales')
                # time.sleep(1.5)
                balance -= bet # Restamos otra vez la apuesta para crear la nueva mano.
                # Crear dos nuevas manos con una carta cada una
                mano1 = [playerHand[0]]
                mano2 = [playerHand[1]]
                # Repartir una carta adicional a cada nueva mano
                dealCard(mano1, deck)
                dealCard(mano2, deck)
                hands = [mano1, mano2]  # Actualizar lista de manos
                apuestas = [bet, bet]  # Duplicar apuestas
        
        # Jugar cada mano (1 o 2 si hizo split)
        for i, mano in enumerate(hands):
            if balance >= apuestas[i] * 2:
                balance -= apuestas[i]  # Paga la apuesta adicional para doblar
                apuestas[i] *= 2
                dealCard(mano, deck)
                hands[i] = mano
                # print(f"Dobló: mano final {mano} con total {total(mano)}")
            else:
                while total(mano) <= 16:
                    dealCard(mano, deck)
                hands[i] = mano
                continue
        
            # Turno del dealer (juega después de todos los jugadores)
            # print(f"\nAhora es el turno del dealer...")
            # time.sleep(1.5)
            while total(dealerHand) <= 16:  # El dealer pide hasta tener 17 o más
                dealCard(dealerHand, deck)

        # print(f"\nDealer tiene {dealerHand} con total {total(dealerHand)}")

        if seguro_apuesta > 0:
            if total(dealerHand) == 21 and len(dealerHand) == 2:  # Dealer tiene blackjack
                seguro_ganancia = seguro_apuesta * 2
                balance += seguro_ganancia
                # print(f"\n¡Dealer tiene Blackjack! Ganas ${seguro_ganancia} del seguro")
                # time.sleep(1)
            else:
               #  print("\nDealer no tiene Blackjack. Pierdes el seguro.")
                # time.sleep(1)
                pass

        # Evaluar resultados de cada mano del jugador
        for i, mano in enumerate(hands):
            jugador = total(mano)
            dealer = total(dealerHand)
            apuesta = apuestas[i]
            ganancia = 0  # Para calcular ganancias/pérdidas

            # print(f"\nEvaluando mano {i+1}: {mano} con total {jugador}")

            # Determinar resultado de la mano
            if jugador == 21 and len(mano) == 2:  # Blackjack natural
                # print("Blackjack! Tú ganas.")
                ganancia = int(apuesta * 1.5)  # Paga 3:2
                ganancia += int(apuesta) # Recupera la apuesta inicial.
            elif jugador > 21:  # Se pasó
                # print("Te pasaste. Pierdes.")
                ganancia += 0
            elif dealer > 21:  # Dealer se pasó
                # print("El dealer se pasó. Tú ganas.")
                ganancia += int(apuesta + apuesta) # Recupera su apuesta y gana el monto a la par de la casa.
            elif jugador > dealer:  # Gana jugador
                # print("Tú ganas.")
                ganancia = int(apuesta + apuesta) # Pasa lo mismo que antes.
            elif jugador < dealer:  # Gana dealer
                # print("El dealer gana.")
                ganancia += 0
            else:  # Empate
                # print("Empate.")
                # print('Se devuelve tu apuesta inicial')
                balance += apuesta # Se devuelve la apuesta

        # time.sleep(1)
        # Actualizar balance con los resultados
        balance += ganancia
        # print(f"\nGanancia total en la ronda: ${ganancia}")
        # print(f"Balance final: ${balance}")

        # Verificar si se quedó sin dinero
        if balance <= 0:
            # print("Te has quedado sin dinero. Fin del juego.")
            break

        # time.sleep(1)
        # Preguntar si quiere seguir jugando
        seguir = 's' # input("\n¿Quieres seguir jugando? (s/n): ").lower()
        if seguir != 's':
            # print("Gracias por jugar. ¡Hasta la próxima!")
            break

    return contador_turnos


# Iniciar el juego
print(jugar_blackjack_doblando(10))


inicio = time.time()
montos = list(range(10, 110, 10))  # [10, 20, ..., 100]
jugadas = [jugar_blackjack_doblando(monto) for monto in montos]


plt.plot(montos, jugadas, marker='o', linestyle='-', color ='grey')
plt.xlabel('Monto inicial')
plt.ylabel('Número de jugadas hasta perder')
plt.title('Relación entre monto inicial y jugadas\n Estrategia: Siempre Dobla')
plt.grid(True)
plt.show()

fin = time.time()
tiempo_ejecucion = fin - inicio
print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")


inicio = time.time()
def promedio_jugadas(monto, repeticiones=100):
    resultados = [jugar_blackjack_doblando(monto) for _ in range(repeticiones)]
    return np.mean(resultados)

jugadas_promedio = [promedio_jugadas(monto) for monto in montos]

plt.plot(montos, jugadas_promedio, marker='o', linestyle='-', color = 'grey')
plt.xlabel('Monto inicial')
plt.ylabel('Promedio de jugadas hasta perder')
plt.title('Relación entre monto inicial y jugadas\nEstrategia: Jugar doblando \n(Promedio de 100 simulaciones)')
plt.grid(True)
plt.show()

fin = time.time()
tiempo_ejecucion = fin - inicio
print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")

    
inicio = time.time()
def promedio_y_desviacion(monto, repeticiones=100):
    resultados = [jugar_blackjack_doblando(monto) for _ in range(repeticiones)]
    return np.mean(resultados), np.std(resultados)

promedios = []
desviaciones = []

for monto in montos:
    prom, std = promedio_y_desviacion(monto)
    promedios.append(prom)
    desviaciones.append(std)

plt.errorbar(montos, promedios, yerr=desviaciones, fmt='-o', capsize=5, color = 'grey')
plt.xlabel('Monto inicial')
plt.ylabel('Jugadas hasta perder (promedio ± std)')
plt.title('Relación entre monto inicial y jugadas\nEstrategia: Jugar doblando con barras de error\nPromedio de 100 simulaciones')
plt.grid(True)
plt.show()

fin = time.time()
tiempo_ejecucion = fin - inicio
print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")



inicio = time.time()
monto = 100
jugadas = [jugar_blackjack_doblando(monto) for _ in range(1000)]

plt.hist(jugadas, bins=30, color='grey', edgecolor='black')
plt.xlabel('Número de jugadas hasta perder')
plt.ylabel('Frecuencia')
plt.title(f'Distribución de jugadas hasta perder (Monto: {monto})')
plt.grid(True)
plt.show()

fin = time.time()
tiempo_ejecucion = fin - inicio
print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")


inicio = time.time()
data = []

for monto in montos:
    for _ in range(100):
        jugadas = jugar_blackjack_doblando(monto)
        data.append({'Monto': monto, 'Jugadas': jugadas})

df = pd.DataFrame(data)
sns.boxplot(x='Monto', y='Jugadas', data=df, color = 'grey')
plt.title('Distribución de jugadas según monto inicial')
plt.show()

fin = time.time()
tiempo_ejecucion = fin - inicio
print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")



inicio = time.time()
rondas = 100
sobrevive = []

for monto in montos:
    cuenta = sum([jugar_blackjack_doblando(monto) > rondas for _ in range(1000)])
    prob = cuenta / 1000
    sobrevive.append(prob)

plt.plot(montos, sobrevive, marker='o', color = 'grey')
plt.xlabel('Monto inicial')
plt.ylabel(f'Probabilidad de sobrevivir > {rondas} jugadas')
plt.title(f'Sobrevivencia después de {rondas} rondas')
plt.grid(True)
plt.show()

fin = time.time()
tiempo_ejecucion = fin - inicio
print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")



monto_fijo = 10
rondas_lista = list(range(10, 201, 10))  # De 10 a 200 en pasos de 10
probabilidades = []

inicio = time.time()

for rondas in rondas_lista:
    cuenta = sum([jugar_blackjack_doblando(monto_fijo) > rondas for _ in range(1000)])
    prob = cuenta / 1000
    probabilidades.append(prob)

plt.plot(rondas_lista, probabilidades, marker='o', color = 'grey')
plt.xlabel('Cantidad de rondas')
plt.ylabel(f'Probabilidad de sobrevivir con {monto_fijo}')
plt.title(f'Sobrevivencia según cantidad de rondas (monto = {monto_fijo})')
plt.grid(True)
plt.show()

fin = time.time()
print(f"Tiempo de ejecución: {fin - inicio:.2f} segundos")


