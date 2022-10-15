s="Serie= ["
rangomax=int(input("Digite el numero de elementos: "))

for i in range (1,rangomax+1):
    if i<rangomax:
        s=s+str(i)+", "
    if i==rangomax:
        s=s+str(i)+"]"

print(s)