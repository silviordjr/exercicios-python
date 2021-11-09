def totalInvestido():
    tempo = int(input("Inforte o tempo de investimento: "))
    taxa = float(input("Informe a taxa de juros (Obs.: unidade de tempo compativel): "))
    aporte = float(input("Informe o valor do aporte mensal: "))

    aux = 0
    montante = 0

    while aux < tempo:
        montante = montante + aporte*((1+(taxa/100))**(tempo - aux))
        aux = aux + 1

    print ("O montante: R$%.2f"%montante)

def aporteMensal():
    tempo = int(input("Informe o tempo de investimentno: "))
    taxa = float(input("Informe a taxa de juros: "))
    montante = float(input("Informe o montante final desejado: "))

    aporte = 0
    aux1 = 0

    while aux1 < montante:
        aux1 = 0
        aux2 = 0
        aporte = aporte + 10
        while aux2 < tempo:
            aux1 = aux1 + aporte*((1+(taxa/100))**(tempo - aux2))
            aux2 = aux2 + 1
    
    print("Você precisará aportar R$%.2f por mês para obter R$%.2f no total."%(aporte,aux1))

def tempoInvestido():
    taxa = float(input("Informe a taxa de juros: "))
    montante = float(input("Informe o montante final desejado: "))
    aporte = float(input("Informe o valor do aporte mensal: "))

    aux1 = 0
    tempo = 1

    while aux1 < montante:
        aux1 = 0
        aux2 = 0
        while aux2 < tempo:
            aux1 = aux1 + aporte*((1+(taxa/100))**(tempo - aux2))
            aux2 = aux2 + 1
        tempo = tempo + 1
    
    print("Você precisará de",tempo,"anos para obter R$%.2f"%aux1)

tipo = int(input("1 - Calculo de aportes mensais \n2 - Calculo de tempo de investimento \n3 - Calculo total investido \nInforme o tipo de calculo: "))

if tipo == 1:
    aporteMensal()
elif tipo == 2:
    tempoInvestido()
else:
    totalInvestido()
