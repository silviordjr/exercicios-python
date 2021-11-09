print ("Menu de opções:\n1 - Soma dois números\n2 - Raiz quadrada de um número")

opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    soma = n1 + n2

    print (n1,"+",n2,"=",soma)

elif opcao == 2:
    from math import sqrt

    n = float(input("Digite o número: "))

    raiz = sqrt(n)

    print ("A raiz quadrada de",n,"é:",raiz)

else:
    print("Opção inválida!")

