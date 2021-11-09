candidato_1 = 0
candidato_2 = 0
candidato_3 = 0

n = int(input("Informe o número de eleitores: "))

print("Digite:\n1 para candidato 1!\n2 para candidato 21\n3 para candidato 3!")

for i in range (1,n+1):
    voto = int(input("Vote no seu candidato! "))

    if voto == 1:
        candidato_1 = candidato_1 + 1
    
    elif voto == 2:
        candidato_2 = candidato_2 + 1
    
    elif voto == 3:
        candidato_3 = candidato_3 + 1
    
    else:
        print ("Voto anulado!")

lista = [candidato_1, candidato_2, candidato_3]
lista.sort()

vencedor = 0

if lista[2] == candidato_1:
    vencedor = 1

elif lista[2] == candidato_2:
    vencedor = 2

elif lista[2] == candidato_3:
    vencedor = 3


print("Candidato 1 obteve",candidato_1,"votos!\nCandidato 2 obteve",candidato_2,"votos!\nCandidato 3 obtebe",candidato_3,"votos!\nO vencedor foi o Candidato",vencedor)


