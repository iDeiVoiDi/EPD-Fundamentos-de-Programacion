import random

print("| Juego Dados 2 Jugadores |")

# Preguntamos los nombres de ambos jugadores
player_1 = input("· Como se llamará el primer jugador?: ")
player_2 = input("· Como se llamará el segundo jugador?: ")

# Generamos los numeros aleatorios de todos los dados
num_1_1 = random.randint(1,6)
num_1_2 = random.randint(1,6)

num_2_1 = random.randint(1,6)
num_2_2 = random.randint(1,6)

# Mostramos el informe con los datos obtenidos
print(f"\n| La diferencia de puntos del primer al segundo jugador es: {(num_1_1 + num_1_2) - (num_2_1 + num_2_2)}") #! Puede ser negativo, pero el ejercicio pide hacerlo asi
print(f"| El resumen de la puntuación es: \n→ {player_1}: {num_1_1 + num_1_2}\n→ {player_2}: {num_2_1 + num_2_2}")
