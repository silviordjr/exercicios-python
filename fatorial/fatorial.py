n = int(input('Digite um numero natural n: '))
fatorial = 1

if n == 0: 
    fatorial = 1
else: 
    while n > 0:
        fatorial = fatorial * n
        n = n - 1

print(fatorial)



