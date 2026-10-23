PLATAFORMAS = ["Xbox", "Playstation", "Nintendo", "PC"]
GENEROS = ["Accion", "Aventura", "RPG", 
    "Mundo Abierto", "Deportes", "Simulacion"]
DIFIULTADES = ["Facil", "Medio", "Dificil"]

VIDEOJUEGOS = [
    ["Minecraft", "Aventura", "PC", "Facil", 30],
    ["Forza Horizon 5", "Deportes", "Xbox", "Medio", 25],
    ["The Witcher 3", "RPG", "Playstation", "Dificil", 100],
    ["Super Mario Odyssey", "Aventura", "Nintendo", "Medio", 15],
    ["Dark Souls III", "RPG", "PC", "Dificil", 40],
    ["EA Sports FC 25", "Deportes", "Playstation", "Facil", 20],
    ["The Legend of Zelda: Breath of the Wild", "Mundo Abierto", "Nintendo", "Medio", 50],
    ["Halo Infinite", "Accion", "Xbox", "Medio", 20],
    ["Cyberpunk 2077", "Mundo Abierto", "PC", "Dificil", 60],
    ["Stardew Valley", "Simulacion", "PC", "Facil", 80]
]

def obtener_genero():
    """ Pide genero del videojuego deseado """
    while True:
        genero = input(
        "¿Qué género te gustaria probar? "
        "(Accion, Aventura, RPG, "
        "Mundo Abierto, Deportes o Simulacion) "
        )
        for opcion in GENEROS:
            if genero.lower() == opcion.lower():
                return opcion

def obtener_plataforma():
    """Pide plataforma deseada"""
    while True:
        plataforma = input(
        "¿Juegas en PlayStation, Nintendo, Xbox o PC? "
        )
        for opcion in PLATAFORMAS:
            if plataforma.lower() == opcion.lower():
                return opcion

def obtener_dificultad():
    """Pide dificultad deseada"""
    while True:
        dificultad = input(
        "¿Qué nivel de dificultad te gustaría? "
        "¿Facil, Medio, Dificil? "
        ).capitalize()
        if dificultad in DIFIULTADES:
            return dificultad

def obtener_duracion():
    """Pide duración deseada en un rango maximo de 800 hr"""
    duracion = int(input(
    "¿Aproximadamente cuantó tiempo quieres "
    "dedicarle (horas)? "
    ))
    semanas = int(input(
        "¿En cuantas semanas quieres terminarlo? "
    ))
    while True:
        if (duracion < 0 or duracion > 800):
            duracion = int(input(
            "Dame un valor correcto para la duración: "
            ))
        elif semanas <= 0:
            semanas = int(input(
                "Dame un valor correcto para semanas"
            ))
        else:
            return duracion, semanas

def horas(duracion, semanas):
    """Calcula las horas invertidas por semana"""
    horas_por_semana = duracion / semanas
    horas_por_semana = round(horas_por_semana, 2)
    return horas_por_semana