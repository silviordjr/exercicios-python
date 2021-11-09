def n_primos(x):
    if x > 1:
        contador = 1
        while 2 < x:
            i = 2
            primo = True
            while i < x:
                if x % i == 0 and primo:
                    primo = False
                i = i + 1
            if primo:
                contador = contador + 1
            x = x - 1
        print (contador)
    else:
        erro()

def erro():
    print("Informe um valor válido!")
                    
