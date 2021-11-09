from math import sqrt

def eh_hipotenusa(x):
    cateto_oposto = 1
    hipotenusa = False
    while cateto_oposto < x and not hipotenusa:
        cateto_adjacente = x
        while cateto_adjacente > 0:
            if x == sqrt(cateto_adjacente*cateto_adjacente + cateto_oposto*cateto_oposto):
                hipotenusa = True
            cateto_adjacente = cateto_adjacente - 1
        cateto_oposto = cateto_oposto + 1
    return hipotenusa

def soma_hipotenusas(x):
    soma = 0
    while x >= 1:
        hipotenusa = eh_hipotenusa(x)
        if hipotenusa:
            soma = soma + x
        x = x - 1
    print (soma)

            
