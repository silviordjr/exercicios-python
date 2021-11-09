i = 1
temp = []

while i <13:
    print("Mês",i)
    temperatura = float(input("informe a temperatura média do mês em °C: "))
    temp.append(temperatura)
    i = i + 1

media = sum(temp)/12

i = 0
mesesDoAno = ["Janeiro,","Fevereiro,","Março,","Abril,","Maio,","Junho,","Julho,","Setembro,","Agosto,","Outubro,","Novembro,","Dezembro,"]
tempAcimaMedia = []
mesAcimaMedia = []

while i < 12:
    if temp[i] > media:
        tempAcimaMedia.append(temp[i])
        mesAcimaMedia.append(mesesDoAno[i])
    i = i + 1

print("A temperatura média foi de",media,"°C.\nAs temperaturas acima da média no ano foram:")

i = 0

while i < len(tempAcimaMedia):
    print (mesAcimaMedia[i],"com temperatura média de",tempAcimaMedia[i],"°C.")
    i = i + 1
