n = int(input())
lista = [0,1]

print(lista[0])
print(lista[1])

while len(lista) <= (n-1):
    novo = lista[-1] + lista[-2]
    lista.append(novo)
    print (lista[-1])

