x,n = input().split(" ")

x = float(x)
n = int(n)

num = 0
ex = 0

def calculaFatorial (num):
    aux = 1
    fatorial = 1

    while aux <= num:
        fatorial = fatorial * aux
        aux = aux + 1
    
    return (fatorial)

while num <= (n-1):
    fatorial = calculaFatorial(num)
    ex = ex + (x**num)/fatorial
    num = num + 1

print("%.5f" %ex)
