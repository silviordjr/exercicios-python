dados = ([10001,"Ana",1.63,"F",23],[10002,"Cleber",1.60,"M",43],[10003,"Claudio",1.73,"M",23],[10004,"Beatriz",1.63,"F",13],
         [10005,"Maria",1.43,"F",10],[10006,"João",2.15,"M",23],[10007,"Silvio",1.87,"M",23],[10008,"Davi",1.63,"M",13],
         [10009,"Amanda",1.83,"F",23],[10010,"Claudio",1.73,"M",44],[10011,"Cássio",1.95,"M",31],[10012,"Fagner",1.69,"M",30],
         [10013,"Gil",1.91,"M",30],[10014,"Danilo",1.84,"M",30],[10015,"Lucas",1.74,"M",19],[10016,"Gabriel",1.72,"M",28],
         [10017,"Cantillo",1.80,"M",25],[10018,"Luan",1.82,"M",27],[10019,"Gustavo",1.74,"M",21],[10020,"Ramiro",1.74,"M",28],
         [10021,"João",1.91,"M",35],[10022,"Boselli",1.84,"M",32],[10023,"Otero",1.74,"M",25],[10024,"Éderson",1.87,"M",21])

nome = []
idade = []
identidade = []
soma = 0
i = 0

while i < len(dados):
    j = i + 1
    while j < len(dados):
        if dados[i][4] == dados[j][4]:  
            soma = soma + 1
            nome.append(dados[i][1])
            nome.append(dados[j][1])
            idade.append(dados[i][4])
            idade.append(dados[j][4])
            identidade.append(dados[i][0])
            identidade.append(dados[j][0])
        j = j + 1
    i = i + 1

i = 0

while i < len(identidade):
    j = i + 1
    while j < len(identidade):
        if identidade[i] == identidade[j]:
            del(nome[j])
            del(identidade[j])
            del(idade[j])
        j = j + 1
    i = i + 1

print("Existem",soma,"pessoas com a mesma idade.\nSão elas:")

i = 0

while i < len(identidade):
    print (nome[i],",",idade[i],"anos.")
    i = i + 1



