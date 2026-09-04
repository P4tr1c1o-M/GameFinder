def datos():
    Gen=input("¿Qué género te gustaria probar? ")
    Plataforma= input("¿En qué plataforma juegas? ")
    Dificultad= input("¿Qué nivel de dificultad te gustaría? ¿Facil, Medio, Dificil? ")
    Duracion= int(input("¿Aproximadamente cuantó tiempo quieres dedicarle (horas)? "))
    if Duracion<0 or Duracion>200:
        Duracion=int(input("Dame un valor correcto para la duración: "))
    else:
        print("Duración valida:", Duracion, "horas")
    
    
    return (Gen, Plataforma, Dificultad, Duracion)

datos()

