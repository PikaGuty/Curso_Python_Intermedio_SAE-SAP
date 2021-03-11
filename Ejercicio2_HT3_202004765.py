d=[0.1,0.05,0.06,0.5,0.12,0.1,0.05,0.06,0.5,0.12]
p=[150,90,1500,175,83,66,850,41,61,45]
canasta = []
total=0

def aplica_funcion_lista(ivaa,descu,tota):
    
    for i in range(10):
        de=desc(i)
        pre=p[i]
        iv=iva(i)
        tot=pre+iv-de
        di= {}
        di['Precio: ']=pre
        di['IVA_aplicado: ']='12%'
        di['IVA: ']=iv
        di['Descuento_aplicado: ']='10%'
        di['Descuento: ']=de
        di['Precio Real: ']=tot
        tota=tota+tot
        canasta.append(di)
        print(di)
        #des = d[i]*100
        #di.append(p[i]:'12%':ivaa(i):des,'%':descu(i))
    return tota

    #for Precio,IVA_aplicado,IVA,Descuento_aplicado,Descuento in di.items():
        #print('\nPrecio: {0}  IVA Aplicado: {1} IVA {2} Descuento aplicado: {3} Descuento: {4}')

def iva(n):
    return p[n]*0.12

def desc(n):
    return p[n]*0.1

#aplica_funcion_lista(iva, desc,total)
print('\n\nTOTAL A CANCELAR: ',aplica_funcion_lista(iva, desc,total))
