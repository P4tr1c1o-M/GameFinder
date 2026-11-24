PLATAFORMAS = ["Xbox", "Playstation", "Nintendo", "PC"]

GENEROS = ["Accion", "Aventura", "RPG", 
    "Mundo Abierto", "Deportes", "Simulacion"]

DIFICULTADES = ["Facil", "Medio", "Dificil"]


def crea_matriz_videojuegos(juegos):
    videojuegos = []
    f = open(juegos, "r")

    for linea in f:
        if "\n"  in linea:
            linea = linea.strip("\n")
        linea = linea.split(", ")
        linea[4] = int(linea[4])
        videojuegos.append(linea)

    f.close()

    return videojuegos

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

        if dificultad in DIFICULTADES:
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

def suma_puntos(plataforma, genero, dificultad, 
    duracion, videojuegos):
    """ Función para sumar puntos y obtener los juegos recomendados """
    mejor_puntaje = 0
    recomendados = []
    duracion_juego = []

    for i in range(len(videojuegos)):
        puntaje = 0

        if plataforma == videojuegos[i][2]:
            puntaje = puntaje + 3

            if genero == videojuegos[i][1]:
                puntaje = puntaje + 3

            if dificultad == videojuegos[i][3]:
                puntaje = puntaje + 2

            if duracion >= videojuegos[i][4]:
                puntaje = puntaje + 2
        
        if puntaje > mejor_puntaje:
            recomendados = [videojuegos[i][0]]
            duracion_juego = [videojuegos[i][4]]
            mejor_puntaje = puntaje

        elif puntaje == mejor_puntaje and puntaje > 0:
            recomendados.append(videojuegos[i][0])
            duracion_juego.append(videojuegos[i][4])

    return recomendados, duracion_juego

def preparar_datos(juegos_recomendados):
    """Prepara los datos para mostrar en consola"""
    juego = ""
    horas = ""
    resultado = "Tus videojuegos recomendados son:\n"
    if len(juegos_recomendados[0]) >= 2:
        juego = "\n".join(juegos_recomendados[0])
        horas = (
            "\n".join(str(x) for x in juegos_recomendados[1])
        )

    else:
        juego = (
            " ".join(juegos_recomendados[0])
        )

        for i in juegos_recomendados[1]:
            horas = "".join(str(i))

    if len(juegos_recomendados[0]) >= 2:
        for i in range(len(juegos_recomendados[0])):
            resultado = resultado + (
                juego.split("\n")[i] + " - " +
                horas.split("\n")[i] + " horas\n"
            )
    else:
        resultado = resultado + juego + " - " + horas + " horas"

    return resultado

"""Main"""
consulta = "si"

while consulta == "si":
    videojuegos = crea_matriz_videojuegos("Juegos.txt")
    plataforma = obtener_plataforma()
    genero = obtener_genero()
    dificultad = obtener_dificultad()
    duracion = obtener_duracion()
    semanas = duracion[1]
    duracion = duracion[0]
    juegos_recomendados = (
    suma_puntos(plataforma, genero, dificultad, duracion, videojuegos)
    )
    print(preparar_datos(juegos_recomendados))

    consulta = input("¿Deseas hacer otra consulta? "
        ).capitalize().lower()

    

print("Gracias por utilizar GameFinder")