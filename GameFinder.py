def datos():
    Gen=input("¿Qué género te gustaria probar? (Acción, Aventura, RPG, Mundo Abierto, Deportes o Simulación) ")
    Plataforma= input("¿Juegas en PlayStation, Nintendo, Xbox o PC? ")
    Dificultad= input("¿Qué nivel de dificultad te gustaría? ¿Facil, Medio, Dificil? ")
    Duracion= int(input("¿Aproximadamente cuantó tiempo quieres dedicarle (horas)? "))
    Sem=int(input("¿En cuantas semanas quieres terminarlo? "))
    if (Duracion<0 or Duracion>800):
        Duracion=int(input("Dame un valor correcto para la duración: "))
    else:
        print("Duración valida:", Duracion, "horas")
        Horasxsemana=Duracion/Sem
        print("Tendrías que jugar aproximadamente", Horasxsemana, "horas por semana")
    
    
    return (Gen, Plataforma, Dificultad, Duracion)

datos()

