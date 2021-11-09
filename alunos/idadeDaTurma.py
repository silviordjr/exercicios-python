lista = []

n = int(input("Digite o número de pessoas: "))

for i in range (1, n+1):
    idade = int(input("Qual a sua idade? "))
    lista.append(idade)

media = sum(lista)/n

if media < 25:
    print("A turma é jovem!")

elif media > 60:
    print("A turma é idosa!")

else:
    print("A turma é adulta!")

