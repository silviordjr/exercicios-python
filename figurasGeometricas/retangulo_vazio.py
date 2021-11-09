largura = int(input("Informe a largura do retângulo: "))
altura = int(input("Informe a altura do retângulo: "))

i = 1
while i <= altura:
    j = 1
    while j <= largura:
        if i == 1 or j == 1 or i == altura or j == largura:
            print("#",end="")
        else:
            print(" ",end="")
        j = j + 1
    print()
    i = i + 1
