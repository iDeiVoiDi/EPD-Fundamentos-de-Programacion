print("| Calculador con IVA |\n")

# Declaramos las constantes
IVA = 0.21

# Preguntamos datos → precio base y unidades
precio_base = float(input("· ¿Cual es el precio base del producto?: (sin IVA) "))
unidades = int(input("· ¿Cuantas unidades fueron compradas?: "))

# Mostramos el informe con los datos obtenidos
print(f"\n| Ticket con los datos y precios:")
print(f"→ Subtotal (Sin IVA): {precio_base * unidades}\n→ IVA: +{(precio_base * unidades) * IVA}\n→ Total: {(precio_base * unidades) * (1 + IVA)}")
