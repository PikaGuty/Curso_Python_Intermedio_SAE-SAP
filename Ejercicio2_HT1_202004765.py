n=int(input("Ingrese el valor de n "))
def ejercicio2(c=1,n1=1,n2=1):
    if c<=n: 
        if c==1 or c==2:
            print(1)
            c+=1
            ejercicio2(c,n1,n2)
        else:
            r=n1+n2
            print(r)
            n2=n1
            n1=r
            c+=1
            ejercicio2(c,n1,n2)
ejercicio2()