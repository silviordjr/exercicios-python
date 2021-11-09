n = int(input())

i = 0
v = []
w = []

while i < n:
    num = int(input())
    v.append(num)
    
    aux = 1
    fatorial = 1

    while aux <= num:
        fatorial = fatorial * aux
        aux = aux + 1
    w.append(fatorial)

    i = i+1

i = 0

while i <= n-1:
    if i == n-1:
         print("{}".format(v[i]))
    else:
        print("{}".format(v[i]),end=' ')
    i = i + 1
i = 0
while i <= n-1:
    print("{}".format(w[i]),end=' ')
    i = i + 1


