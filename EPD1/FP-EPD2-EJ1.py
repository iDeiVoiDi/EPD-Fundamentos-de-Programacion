print("| Billete Autobuses |\n")

# Constantes (Se pueden editar desde aqui)
# Todas funcionan como porcentage en nº entre 0 y 1
DESCUENTO_COSTA_DEL_SOL = 0.15
DESCUENTO_SIERRA_NEVADA = 0.2
DESCUENTO_MADRID = 0.1

# Recolección de los datos del usuario
precio_billete_original = float(input("• ¿Cuanto es el precio original del billete?: "))
destino = input("• ¿Cual será su destino?: ")
temporada = input("• ¿Cual será la temporada en la que se realizará?: ")

# Lógica del programa
aplicacion_descuento = False
if destino == "Costa del Sol" and temporada == "verano":
    precio_billete_final = (1 - DESCUENTO_COSTA_DEL_SOL) * precio_billete_original
    aplicacion_descuento = True

if destino == "Sierra Nevada" and temporada == "invierno":
    precio_billete_final = (1 - DESCUENTO_SIERRA_NEVADA) * precio_billete_original
    aplicacion_descuento = True

if destino == "Madrid":
    precio_billete_final = (1 - DESCUENTO_MADRID) * precio_billete_original
    aplicacion_descuento = True

# Muestra de los datos obtenidos
if aplicacion_descuento:
    print("| Aplicación del descuento:" \
    f"→ Pasa de {precio_billete_original}€ a {precio_billete_final}€")