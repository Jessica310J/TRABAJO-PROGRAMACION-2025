# Crear un diccionario con información personal
informacion_personal = {
    "nombre": "Amy Piedra",
    "edad": 45,
    "ciudad": "Macas",
    "profesion": "Ingeniera"
}

# Acceder al valor de la clave 'ciudad' y modificarlo
informacion_personal["ciudad"] = "Guayaquil"

# Agregar una nueva clave-valor para la profesión
informacion_personal["profesion"] = "Arquitecta"

# Verificar si la clave 'telefono' existe
if "telefono" not in informacion_personal:
    # Agregar un número de teléfono ficticio
    informacion_personal["telefono"] = "+593-97229353"

# Eliminar la clave 'edad'
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")
