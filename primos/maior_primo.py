def maior_primo(x):
    while x > 1:
        n = 2
        primo = True
        while n < x:
            aux = x % n 
            if aux == 0:
                primo = False
                break
            n = n + 1
        if not primo:
            x = x - 1
        else:
            return x




