lista = [1,2,3,4,5,6,7,8,9,10]

print("A lista pré definida é: ",lista)

posicao = int(input("Informe a posição desejada: "))
elemento = float(input("informe o elemento desejado: "))

el = [elemento]

inicio = lista[:]
del(inicio[posicao:])

fim = lista[:]
del(fim[:posicao])

lista_final = inicio + el + fim

print(lista_final)