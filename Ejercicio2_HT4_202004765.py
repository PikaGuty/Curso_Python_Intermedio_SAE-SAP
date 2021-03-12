n=int(input('Ingrese un numero para conocer su tablas de multiplicar:  '))
nn=str(n)
i=0
tabla='Tabla de multiplicar de '+ str(n)+'\n\n'
tabla
f=open("Tabla de multiplicar.txt","w")
for i in range(11):
    mul=i*n
    tabla=tabla+str(i)+' * '+nn+' = '+str(i*n)+"\n"
    

f.write(tabla)
f.close()
print('Se ha generado un archivo txt con la tabla de multiplicar')