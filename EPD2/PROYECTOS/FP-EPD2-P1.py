print("| Piedra Papel y Tijeras |\n")

# Marco las constantes
POSIBILIDADES = ["piedra", "papel", "tijera"]

# Marco las variables de estado
resultados = 0

# Recolección de los datos del usuario
jugador_1 = input("• ¿Que saca el Jugador 1?: (piedra/papel/tijera)")
jugador_2 = input("• ¿Que saca el Jugador 2?: (piedra/papel/tijera)")

# Lógica del programa
if jugador_1 in POSIBILIDADES and jugador_2 in POSIBILIDADES:

    # Le asignamos los valores numericos de la lista de POSIBILIDADES
    if jugador_1 == "piedra": jugador_1 = 0
    elif jugador_1 == "papel": jugador_1 = 1
    else: jugador_1 = 2

    if jugador_2 == "piedra": jugador_2 = 0
    elif jugador_2 == "papel": jugador_2 = 1
    else: jugador_2 = 2

    # Como los valores de la lista son conocidos, el anterior es derrotado por la posicion elegida
    if jugador_1 - 1 == jugador_2 or (jugador_1 == 0 and jugador_2 == 2):
        resultados = 1
    else:
        resultados = 2

else:
    print("| Hubo problemas !!")

# Muestra de los datos obtenidos
if resultados == 1:
    print("→ GANADOR JUGADOR 1")
if resultados == 2:
    print("→ GANADOR JUGADOR 2")
if resultados == 0:
    print("→ EMPATE")