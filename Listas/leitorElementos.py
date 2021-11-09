n = int(input())

i = 0
vet = []
while i < n:
    num = float(input())
    vet.append(num)
    i = i + 1

vet.sort()

media = sum(vet)/n

i = 0
aux = 0

while i < n:
    if vet[i]%2 == 0:
        aux = aux + 1
    i = i + 1

pares = 100*(aux/n)

print("%.1f" %vet[0])
print("%.1f" %vet[-1])
print("%.2f" %pares)
print("%.2f" %media)