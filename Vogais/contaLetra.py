def vezesLetraAparece(frase, letra):
    texto = list(frase)
    i = 0
    soma = 0

    while i < len(texto):
        if texto[i] == letra:
            soma = soma + 1
        
        i = i + 1
    
    print (soma)

if __name__ == '__main__':
    frase = "oi, eu sou o goku"
    letra = "o"
    vezesLetraAparece(frase, letra)

