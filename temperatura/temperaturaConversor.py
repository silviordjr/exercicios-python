def fahrenheit(T):
    return ((float(9)/5)*T + 32)

temperatura = [0,34,23,12,43,54,3,2,1,35,-54,-9,0,-9,-2,34]

for temp in map(fahrenheit,temperatura):
    print (temp)

