s="Serie= "
rangomax=int(input("Digite el numero maximo: "))

for i in range(2, rangomax+1): 
    for j in range(2,i): 
            if(i % j==0): 
                break
    else: 
        s=s+str(i)+", "
      
print(s)