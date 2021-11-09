n = int(input())

i = 0
matriz = []
vetor = 1

while i < (n**2):
    num = int(input())
    matriz.append(num)
    i = i + 1

aux = 0
while aux < (n**2):
    vetor = vetor*matriz[aux]
    
    aux = aux + n + 1

print(vetor)

