def decomposicao():
    n = int(input("Digite o número a ser decomposto: "))
    if n >= 2:
        i = 2
        while i <= n:
            contador = 0
            while n % i == 0:
                contador = contador + 1 
                n = n // i
            if n % i != 0 and contador > 0:
                print(i,"^",contador,end = "*")  
                i = i + 1 
            elif  n % i != 0:
                i = i + 1
    else: 
        erro()

def erro():
    print("Digite um numero que possa ser decomposto!")

decomposicao()