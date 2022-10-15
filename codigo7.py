s="Serie= "
rangomax=int(input("Digite el numero de elementos: "))

for i in range (1,rangomax+1):
    if i!=rangomax:
        s=s+str(i**(i-1))+"/"+str(2*i + 1) + ", "
    if i==rangomax:
        s=s+str(i**(i-1))+"/"+str(2*i + 1)

print(s)