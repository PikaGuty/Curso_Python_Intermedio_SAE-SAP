frutas={'Platano':1.35,'Manzana':0.8,'Pera':0.85,'Naranja':0.7}

print('')
eleccion=input('¿Que fruta deseas?  ').title()
print('')
print('')
kg = float(input('¿Cuantos kilos deseas?  '))
print('')
print('')

if eleccion in frutas:
    total=(frutas[eleccion]*kg)
    print('Te llevas ',kg,' de ',eleccion,' tienes que pagar: ',total)
    print('')
    print('')
else:
    print('No tenemos ',eleccion)
    print('')
    print('')