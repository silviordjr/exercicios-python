x,y,n = input().split(" ")

x = int(x)
y = int(y)
n = int(n)

f = [x,y]
i = 1

print (f[0])
print (f[1])

while i <= (n-2):
    if i%2 == 0:
        num = f[-1] - f[-2]
    else:
        num = f[-2] + f[-1]
    f.append(num)
    print(f[-1])
    i = i + 1

