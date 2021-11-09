def recebeVetor(n):
    i = 0 
    vet = []
    while i < n:
        num = float(input())
        vet.append(num)
        i = i + 1
    
    return vet

def calculaProduto(vet,vet2):
    i = 0
    soma = 0

    while i <= (n-1):
        produto = vet[i]*vet2[i]
        soma = soma + produto
        i = i + 1
    
    imprime(soma)

    return (soma)

def imprime (soma):
    print (soma)



n = int(input())
vet = recebeVetor(n)
vet2 = vet[:]
vet = recebeVetor(n)
calculaProduto(vet,vet2)


