# Escritura en el archivo
file_path = 'my_notes.txt'  # Definimos la ruta del archivo

# Usamos 'with open()' para asegurarnos de que el archivo se cierre automáticamente después
with open(file_path, 'w') as file:  # Abrimos el archivo en modo escritura ('w')
    # Escribimos notas personales en el archivo
    file.write("Nota 1: No olvides hacer el práctico experimental de Fundamentos de Tecnologías, es crucial para la nota.\n")  # Escribimos la primera nota
    file.write("Nota 2: Dedica tiempo a investigar y comprender bien los conceptos del práctico experimental de Fundamentos de Tecnologías.\n")  # Escribimos la segunda nota
    file.write("Nota 3: Planifica y organiza tu tiempo para completar con éxito el práctico experimental de Fundamentos de Tecnologías.\n")  # Escribimos la tercera nota

print(f"Archivo '{file_path}' creado y escrito con éxito.")  # Confirmamos que el archivo se creó y escribió

# Lectura del archivo
file_path = 'my_notes.txt'  # Definimos la ruta del archivo

# Usamos 'with open()' para asegurarnos de que el archivo se cierre automáticamente después
with open(file_path, 'r') as file:  # Abrimos el archivo en modo lectura ('r')
    lines = file.readlines()  # Leemos todas las líneas del archivo y las almacenamos en una lista

print("\nContenido del archivo leído línea por línea:")  # Indicamos que vamos a mostrar el contenido del archivo
for line in lines:  # Iteramos sobre cada línea en la lista de líneas
    print(line.strip())  # Imprimimos cada línea eliminando los espacios en blanco al principio y al final
