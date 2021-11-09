def recebeVetor(n):

    i = 0
    vet = []

    while i < n:
        num = float(input())
        vet.append(num)
        i = i + 1
    
    calculaMenor(vet)

    return vet

def calculaMenor(vet):

    vet.sort()
    menor = vet[0]

    imprime(menor)

    return(menor)

def imprime(menor):
    print(menor)
    

n = int(input())
recebeVetor(n)
