n=int(input("Ingrese el número del que desea conocer su factorial "))
def ejercicio3(c=1,r=1):
    if c<=n: 
        if c==0:
            r=r*1
            c+=1
            ejercicio3(c,r)
            
        else:
            r=r*c
            c+=1
            ejercicio3(c,r)
        if c==n+1:
            print(r)
       
ejercicio3()
