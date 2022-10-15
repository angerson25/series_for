s="Serie= "
rangomax=int(input("Digite el numero de elementos: "))

for i in range (1,rangomax+1):
    if 1<=i<rangomax:
        s=s+str(i**2)+", "
    if i==rangomax:
        s=s+str(i**2)

print(s)