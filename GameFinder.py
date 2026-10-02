PLATAFORMAS = ["Xbox", "Playstation", "Nintendo", "PC"]
GENEROS = ["Acción", "Aventura", "RPG", 
    "Mundo Abierto", "Deportes", "Simulación"]
DIFIULTADES = ["Facil", "Medio", "Dificil"]


def obtener_genero():
    """ Pide genero del videojuego deseado """
    while True:
        genero = input(
        "¿Qué género te gustaria probar? "
        "(Acción, Aventura, RPG, "
        "Mundo Abierto, Deportes o Simulación) "
        )
        if genero in GENEROS:
            return genero

def obtener_plataforma():
    """Pide plataforma deseada"""
    while True:
        plataforma = input(
        "¿Juegas en PlayStation, Nintendo, Xbox o PC? "
        )
        if plataforma in PLATAFORMAS:
            return plataforma


def obtener_dificultad():
    """Pide dificultad deseada"""
    while True:
        dificultad = input(
        "¿Qué nivel de dificultad te gustaría? "
        "¿Facil, Medio, Dificil? "
        )
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
    if (duracion < 0 or duracion > 800):
        duracion = int(input(
            "Dame un valor correcto para la duración: "
        ))
    else:
        return duracion, semanas


def horas(duration, semanas):
    """Calcula las horas invertidas por semana"""
    horas_por_semana = duration / semanas
    horas_por_semana = round(horas_por_semana, 2)
    return horas_por_semana