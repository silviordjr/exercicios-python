def calculadoraAdicaoSubtracao(numero, outroNumero, operacao):
    if operacao == "+":
        resultado = numero + outroNumero
    elif operacao == "-":
        resultado = numero - outroNumero
    else:
        resultado = 0
    
    print (resultado)

if __name__ == '__main__':
    numero = 3
    outroNumero = 5
    operacao = "+"

    calculadoraAdicaoSubtracao(numero, outroNumero, operacao)