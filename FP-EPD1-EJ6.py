print("| Rendimiento Cosecha |\n")

# Preguntamos datos → tipo de cultivo, tamaño sembrado y kg conseguidos
tipo_cultivo = input("· ¿Que tipo de cultivo fue sembrado?: ") 
espacio_usado = float(input("· ¿Cuantas hectáreas fueron sembradas?: "))
kg_ganados = float(input("· ¿Cuantos kg fueron cosechados?: "))

# Mostramos el informe con los datos obtenidos
print(f"| El rendimiento de la cosecha es de: {kg_ganados / espacio_usado} kg/hectarea de {tipo_cultivo}")