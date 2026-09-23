print("| Revisión Fábrica |\n")

# Preguntamos datos → objetivo dirario, unidades turno mañana y tarde
objetivo_diario = int(input("· ¿Cual es el objetivo diario?: "))
unidades_mañana = int(input("· ¿Cuantas unidades se fabricaron en el turno de la mañana?: "))
unidades_tarde = int(input("· ¿Cuantas unidades se fabricaron en el turno de la tarde?: "))

# Mostramos el informe con los datos obtenidos
print(f"\n| Informe diario de la producción: ")
print(f"→ Unidades Totales: {unidades_mañana + unidades_tarde}") 
#! Puede ser negativo, pero el ejercicio pide hacerlo asi
print(f"→ Diferencia respecto Objetivo: {(unidades_mañana + unidades_tarde) - objetivo_diario}")