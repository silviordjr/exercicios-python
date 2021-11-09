n = int(input())

i = 0 
num = 1
s = 0

while i < n:
    if i == 0 or i%2 == 0:
        s = s + 1/(num**3)
    else:
        s = s - 1/(num**3)
    
    i = i + 1
    num = num + 2

p = (s*32)**(1/3)

print ("%.5f" %p)

