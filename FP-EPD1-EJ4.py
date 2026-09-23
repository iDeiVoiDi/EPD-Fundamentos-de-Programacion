print("| Calculador restaurante |\n")

# Preguntamos datos → precio comida y bebidas y propina
precio_comida = float(input("· ¿Cuanto es el coste de la comida?: "))
precio_bebida = float(input("· ¿Cuanto es el coste de la bebida?: "))
propina = float(input("· ¿Cuanto porcentaje de propina se desea dejar sobre el subtotal?: (Ej. 10 15 20) "))

# Mostramos el informe con los datos obtenidos
print(f"\n| Ticket con los datos y precios:")
print(f"→ Comida: {precio_comida}€\n→ Bebida: {precio_bebida}€\n→ Subtotal: {precio_comida + precio_bebida}€")
print(f"→ Propina: +{(precio_comida + precio_bebida) * (propina / 100)}\n→ Total: {(precio_comida + precio_bebida) * (1 + (propina / 100))}")