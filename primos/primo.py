x = int(input("Digite um número inteiro: "))

i = 2
primo = True

while i < x:
    aux = x % i
    if aux == 0:
        primo = False
        break
    i = i+1

if primo: 
    print("primo")
else:
    print ("não primo")



