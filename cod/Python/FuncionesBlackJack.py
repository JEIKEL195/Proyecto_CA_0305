from BlackJackSimuladoModulo import BlackJackSimulador


def ejecutar_simulacion(estrategia = 'quedarse', monto_inicial = 10, repeticiones = 100, rondas = 50):
    """
    Ejecuta una simulación completa de Blackjack con gráficos.

    Parámetros:
    -----------
    estrategia (str): Nombre de la estrategia a utilizar.
    monto_inicial (int): Monto inicial con el que se empieza.
    repeticiones (int): Número de simulaciones por monto.
    rondas (int): Número de rondas para evaluar probabilidad de sobrevivencia.

    Retorna:
    --------
    None
    """

    montos = list(range(10, 110, 10))
    simulador = BlackjackSimulador(estrategia = estrategia, monto_inicial = monto_inicial, repeticiones = repeticiones)

    print(simulador)
    resultados = simulador.simular(montos)

    simulador.graficar(resultados)
    print('')  # Separador
    simulador.histograma(resultados, monto = 10)
    print('')
    simulador.boxplot(resultados)
    print('')
    simulador.graficar_probabilidad_sobrevivencia(resultados, rondas = rondas)

def comparar_estrategias(repeticiones = 100):
    """
    Compara múltiples estrategias de Blackjack graficando el número promedio de jugadas hasta perder.

    Parámetros:
    -----------
    repeticiones (int): Número de repeticiones por estrategia y monto.

    Retorna:
    --------
    None
    """
    estrategias = ['quedarse', 'como casa', 'siempre doblar', 'quedarse y tomar seguro', 'siempre split']
    montos = list(range(10, 110, 10))
    resultados_todas = {}

    for estrategia in estrategias:
        simulador = BlackjackSimulador(estrategia = estrategia, monto_inicial = 10, repeticiones = repeticiones)
        resultados = simulador.simular(montos)
        resultados_todas[estrategia] = resultados

    plt.figure(figsize = (10, 6))

    for estrategia, resultados in resultados_todas.items():
        promedios = [np.mean(resultados[m]) for m in montos]
        plt.plot(montos, promedios, marker = 'o', label = estrategia.title())

    plt.xlabel('Monto inicial')
    plt.ylabel('Jugadas promedio hasta perder')
    plt.title(f'Comparación de estrategias en Blackjack\n({repeticiones} repeticiones por monto)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def comparar_probabilidad_sobrevivencia(repeticiones = 100):
    """
    Compara la probabilidad de sobrevivir más de cierto número de rondas para distintas estrategias de Blackjack.

    Parámetros:
    -----------
    repeticiones (int): Número de repeticiones por estrategia y monto.

    Retorna:
    --------
    None
    """
    estrategias = ['quedarse', 'como casa', 'siempre doblar', 'quedarse y tomar seguro', 'siempre split']
    montos = list(range(10, 110, 10))
    rondas = 100
    resultados_todas = {}

    # Simulaciones
    for estrategia in estrategias:
        simulador = BlackjackSimulador(estrategia = estrategia, monto_inicial = 10, repeticiones = repeticiones)
        resultados = simulador.simular(montos)
        resultados_todas[estrategia] = resultados

    # Gráfico
    plt.figure(figsize = (10, 6))

    for estrategia, resultados in resultados_todas.items():
        probs = [np.mean(np.array(resultados[m]) > rondas) for m in montos]
        plt.plot(montos, probs, marker = 'o', label = estrategia.title())

    plt.xlabel('Monto inicial')
    plt.ylabel(f'Probabilidad de sobrevivir > {rondas} rondas')
    plt.title(f'Comparación de probabilidad de sobrevivencia\n({repeticiones} repeticiones por monto)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()