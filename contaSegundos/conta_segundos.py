segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segundos // (3600 * 24)

segundos = segundos - dias * (3600 * 24)

horas = segundos // 3600

segundos = segundos - horas * 3600

minutos = segundos // 60

segundos = segundos - minutos * 60

print(dias, "dias, ", horas, "horas, ", minutos, "minutos e ", segundos, "segundos")
