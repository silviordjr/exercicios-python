largura = int(input("Informe a largura do retângulo: "))
altura = int(input("Informe a altura do retângulo: "))

i = 1
while i <= altura:
    j = 1
    while j <= largura:
        print("#",end="")
        j = j + 1
    print()
    i = i + 1
