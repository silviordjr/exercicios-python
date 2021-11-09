from math import sqrt

a = float(input("Informe a: "))
b = float(input("Informe b: "))
c = float(input("Informe c: "))

delta = b*b - 4*a*c

if delta < 0:
    print("esta equação não possui raízes reais")
elif delta == 0:
    x = -b / (2*a)
    print ("a raiz dessa equação é ", x)
else:
    x1 = (-b + sqrt(delta)) / (2*a)
    x2 = (-b - sqrt(delta)) / (2*a)
    if x1 > x2:
        print("as raízes dessa equação são ", x2, "e", x1)
    else:
        print("as raízes dessa equação são ", x1, "e", x2)

