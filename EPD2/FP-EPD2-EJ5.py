print("| Sugerencia Alimentación |\n")

# Recolección de los datos del usuario
hora = int(input("• ¿Que hora es?: (0h-23h) "))

# Lógica del programa + Muestra de los datos
print("| Análisis de posibilidades...")
if hora >= 7 and hora <= 10:
    print("→ RECOMENDADO DESAYUNAR")
elif hora >= 13 and hora <= 15:
    print("→ RECOMENDADO COMER")
elif hora >= 20 and hora <= 22:
    print("→ RECOMENDADO CENAR")
elif hora >= 24 or hora <= 0:
    print("→ HORA NO RECONOCIDA")
else: 
    print("→ HORA NO RECOMENDADA | considera un snack saludable |")
