N=int(input("Valeur de N? "))
U=N
L=[N]
T=0
Z=0
while U!=1:
     if U%2==0:
        U=(U//2)
     else :
        U=(3*U+1)
     L.append(U)
     T=T+1
     if U>N:
        Z=Z+1
     ln=len(L)
     A=max(L)
print ("Trajectoire",L)
print ("Longueur", ln )
print ("Altitude", A)
print ("Temps de vol",T)
print ("Temps de vol en altitude", Z-1)
