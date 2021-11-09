def eh_primo():
    repeticao = True
    while repeticao:
        print("Digite 0 para encerrar.")
        x = int(input("Informe o numero desejado: "))
        if x  > 2:
            i = 2
            primo = True
            while i < x:
                if x % i == 0 and primo:
                    primo = False
                else: 
                    i = i + 1
            if primo:
                print("O número",x,"é primo.")
            else:
                print("O número",x,"não é primo.")
        elif x == 2 or x == 1:
            print("O número",x,"é primo.")
        elif x == 0:
            repeticao = False
        else: 
            erro()

def erro():
    print("Informe um número válido!")
