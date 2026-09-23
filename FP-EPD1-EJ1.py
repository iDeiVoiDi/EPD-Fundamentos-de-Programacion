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

# Calculamos la puntuacion total de cada jugador y su diferencia
puntuacion_1 = num_1_1 + num_1_2
puntuacion_2 = num_2_1 + num_2_2

#! Puede ser negativo, pero el ejercicio pide hacerlo asi
diferencia = puntuacion_1 - puntuacion_2  

# Imprimimos los resultados por pantalla del resultado
print(f"| La diferencia de puntos del primer al segundo jugador es: {diferencia}")
print(f"| El resumen de la puntuación es: \n→{player_1}: {puntuacion_1}\n→{player_2}: {puntuacion_2} ")
