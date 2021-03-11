def aplica_funcion_lista(funcion,lista):
    l=[]
    for i in lista:
        l.append(funcion(i))
    return l

def cuadrado(n):
    return n*n

print(aplica_funcion_lista(cuadrado, [1,2,3,4,5,6,7,8,9,10]))
