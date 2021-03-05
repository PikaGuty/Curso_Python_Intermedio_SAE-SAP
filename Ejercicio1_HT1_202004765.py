def ejercicio1(intento=1):
    respuesta=input("¿De qué color es la fruta? ")
    x=respuesta.upper()
    if x!="NARANJA":
        if intento<3:
            print("\n Fallaste tu ",intento,"intento")
            intento+=1
            ejercicio1(intento)
        else:
            print("\n Perdiste, has fallado en todos tus intentos")
    else:
        print("\n Has Ganado!!!!")

ejercicio1()