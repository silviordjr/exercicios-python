def AplicativoDeFatoracao ():
    fatorar =  True
    while fatorar:
        x = int(input("Digite o numero a fatorar: "))
        fatoracao = 1
        if x > 0:
            y = x
            while y >= 1:
                fatoracao = fatoracao * y
                y = y - 1
            print (x,"!","=",fatoracao)
        elif x == 0: 
            print (x,"!","=",fatoracao)
            fatorar = False
            print ("Fim")
        else: 
            erro()
        

def erro():
    print("Digite um número fatorável!")


        
        







