print("| Piedra Papel y Tijeras |\n")

# Marco las constantes
POSIBILIDADES = ["piedra", "papel", "tijera"]

# Marco las variables de estado
posible = False
victoria_1 = False
victoria_2 = False
empate = False

# Recolección de los datos del usuario
jugador_1 = ("• ¿Que saca el Jugador 1?: (piedra/papel/tijera)")
jugador_2 = ("• ¿Que saca el Jugador 2?: (piedra/papel/tijera)")

# Lógica del programa
if jugador_1 in POSIBILIDADES and jugador_2 in POSIBILIDADES:

    # Le asignamos los valores numericos de la lista de POSIBILIDADES
    if jugador_1 == "piedra": jugador_1 = 0
    elif jugador_1 == "papel": jugador_1 = 1
    else: jugador_1 = 2

    if jugador_2 == "piedra": jugador_2 = 0
    elif jugador_2 == "papel": jugador_2 = 1
    else: jugador_2 = 2

    if jugador_1 - 1:
        if jugador_1 == -1: jugador_1 = 2