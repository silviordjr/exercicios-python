n = int(input())

i = 0

Alunos = []
Ab1 = []
Ab2 = []
Media = []
Situacao = []

while i < n:

    nome = str(input())
    ab1 = float(input())
    ab2 = float(input())

    media = (ab1 + ab2)/2

    if media >= 7:
        situacao = "AP"
    else: 
        situacao = "RP"

    Alunos.append(nome)
    Ab1.append(ab1)
    Ab2.append(ab2)
    Media.append(media)
    Situacao.append(situacao)

i = 0

while i < n:
    print("Nome:",Alunos[i])
    print("AB1:",Ab1[i])
    print("AB2:",Ab2[i])
    print("Media",Media[i])
    print("Situacao",Situacao[i])
