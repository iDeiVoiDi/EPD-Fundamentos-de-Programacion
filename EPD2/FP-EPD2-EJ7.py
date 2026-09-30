print("| Análisis de Días del Mes |\n")

# Marco las constantes
dias_31 = ["enero", "marzo", "mayo", "julio", "agosto", "octubre", "diciembre"]
dias_30 = ["abril", "junio", "septiembre", "noviembre"]
dias_28 = ["febrero"]

# Marco las variables de estado
posible = True
reconocido = False

# Recolección de los datos del usuario
mes = input("• ¿Cual mes quieres validar?: ")
dia = int(input("• ¿Cual dia quieres validar?: "))

# Lógica del programa
if mes in dias_31 or mes in dias_30 or mes in dias_28:
    reconocido = True

    if dia < 0:
        posible = False
    elif mes in dias_28 and dia > 28:
        posible = False
    elif mes in dias_30 and dia > 30:
        posible = False
    elif mes in dias_31 and dia > 31:
        posible = False

# Muestra de los datos obtenidos
print("| Análisis de la viabilidad...")
if not reconocido:
    print("→ MES NO RECONOCIDO")
elif not posible:
    print("→ FECHA INVALIDA")
else:
    print("→ FECHA VALIDA")