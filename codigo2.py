s="Serie= "
rangomax=int(input("Digite el numero de elementos: "))

for i in range (1,rangomax+1):
    if i<rangomax:
        s=s+str(2**i)+", "
    if i==rangomax:
        s=s+str(2**i)

print(s)