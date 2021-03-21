print("-=Vamos descobrir quantos números primos há num intervalo!=-")
num1 = int(input("Digite o número de intervalo inicial:"))
num2 = int(input("Digite o número de intervalo final:"))
pri = 0
for c1 in range(num1,num2,1):
    i = 0
    for c2 in range(1,10,1):
        if(c1%c2==0):
            i+=1
        if(i>=3):
            pri += 1
            break
print("Há %i números primos entre %i e %i."%(pri,num1,num2))