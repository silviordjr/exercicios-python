n,x = input().split(" ")

x = int(x)
n = int(n)

i = 0
matriz = []
vetor = []

while i < (n**2):
    num = int(input())
    matriz.append(num)
    i = i + 1

aux = 0
while aux < (n**2):
    if matriz[aux]%x == 0:
        vetor.append(matriz[aux])
    
    aux = aux + n + 1

if not vetor:
    print("NMDX")
else:
    print(*vetor)


