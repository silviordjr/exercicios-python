def imprimir (rad):
    i = 0
    while i in range (len(rad)):
        print ("%.5f" %rad[i])
        i = i + 1

def converter (graus):
    rad = []

    i = 0

    while i in range(len(graus)):
        from math import pi

        r = graus[i]*pi/180

        rad.append(r)

        i = i + 1
    
    imprimir(rad)
    
    return (rad)

n = int(input())
    
i = 0
graus = []

while i < n:
    num = float(input())
    graus.append(num)
    i = i + 1

converter(graus)
    
