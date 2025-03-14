temperaturas = [
    [   # Ciudad  Quito
        [   # Semana 1
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 13},
            {"day": "Miércoles", "temp":19},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp":16}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp":18},
            {"day": "Domingo", "temp": 16}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp":16},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 16}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 18}
        ]
    ],
    [   # Ciudad  Guayaquil
        [   # Semana 1
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 31}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 31}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 31}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 32}
        ]
    ],
    [   # Ciudad  Macas
        [   # Semana 1
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 31}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp":32},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 32}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 31}
        ]
    ]
]

# Lista de nombres de ciudades para facilitar la lectura de los resultados
ciudades = ["Quito", "Guayaquil", "Macas"]

def calcular_promedio_total_temperaturas(temperaturas, ciudades):
    """
    Calcula e imprime el promedio total de temperaturas para cada ciudad
    durante todas las semanas registradas.

    Args:
        temperaturas (list): Lista 3D con datos de temperaturas.
        ciudades (list): Lista con los nombres de las ciudades.
    """
    for ciudad_idx, ciudad in enumerate(temperaturas):
        total_temperaturas = 0
        total_dias = 0

        for semana in ciudad:
            for dia in semana:
                total_temperaturas += dia["temp"]
            total_dias += len(semana)

        promedio_total = total_temperaturas / total_dias if total_dias > 0 else 0
        print(f"Promedio total de temperaturas en {ciudades[ciudad_idx]}: {promedio_total:.2f} °C")

# Llamamos a la función para ejecutar el cálculo e imprimir los resultados
calcular_promedio_total_temperaturas(temperaturas, ciudades)

