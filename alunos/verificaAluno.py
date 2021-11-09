lista = []
bimestre = 1

for i in range (1,5):
    print ("Bimesrte", bimestre)
    trabalho = float(input("Digite a nota do trabalho do bimestre: "))
    prova = float(input("Digite a nota da prova do bimestre: "))

    media_bimestral = 0.7*prova + 0.3*trabalho

    print ("A média do bimestre", bimestre,"foi:", media_bimestral)

    lista.append(media_bimestral)

    bimestre = bimestre + 1

media_anual = sum(lista)/4

print("A media anual foi:",media_anual)

if media_anual >= 7:
    print("Aluno aprovado!")
elif media_anual < 5:
    print("Aluno reprovado!")
else:
    print ("Aluno na prova final!")
