populacao_a = 80000
populacao_b = 200000
anos = 0

while populacao_a <= populacao_b:
    populacao_a = populacao_a * 1.03
    populacao_b = populacao_b * 1.015
    anos = anos + 1
    print(populacao_a,",",populacao_b,",",anos)

print("A população do país A supera a populção do país B em",anos,"anos")