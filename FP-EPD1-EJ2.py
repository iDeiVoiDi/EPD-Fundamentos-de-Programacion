print("| Gestión de Alimento |")

# Preguntamos datos → alimento, stock y animales
nombre_alimento = input("· ¿Que tipo de alimento será?: ") 
stock_inicial = float(input("· ¿Que cantidad de alimento tendrá?: "))
cantidad_animal = int(input("· ¿Cuantos animales habrá?: "))

# Cuentas para sacar los datos del stock final
#! Puede ser < 0, pero el programa no pide que hacer en esos casos
consumo = (cantidad_animal * 0.25) * 7

# Mostramos el informe con los datos obtenidos
print(f"\n| Informe:\n→ Stock Inicial: {stock_inicial}\n→ Consumo semanal: {consumo}\n→ Stock Final: {stock_inicial - consumo}")
