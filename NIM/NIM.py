def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    SuaJogada = False
    if n % (m+1) == 0: 
        SuaJogada = True
        print ("Você começa!")
        jogada = usuario_escolhe_jogada(n,m)
    else: 
        print("Computador começa!")
        jogada = computador_escolhe_jogada(n,m)
    n = n - jogada
    while n > 0:
        if SuaJogada:
            print("Agora restam",n,"peças no tabuleiro.")
            jogada = computador_escolhe_jogada(n,m) # inserir estratégia do computador
            n = n - jogada
            SuaJogada = False
            #print("Agora restam",n,"peças no tabuleiro.")
        else: 
            print("Agora restam",n,"peças no tabuleiro.")
            jogada = usuario_escolhe_jogada(n,m) # pedir estratégia do usuário
            if jogada > m or jogada > n:
                jogada_invalida()
            else:
                n = n - jogada
                SuaJogada = True
                #print("Agora restam",n,"peças no tabuleiro.")
    if SuaJogada:
        print("Parabéns, você venceu!")
    else: 
        print("Computador venceu!")
    return SuaJogada

def usuario_escolhe_jogada(n,m):
    jogada = int(input("Quantas peças você vai tirar? "))
    print("Você tirou",jogada,"peças.")
    return jogada
    
def computador_escolhe_jogada(n,m):
    jogada = m
    while jogada > 0:
        if (n - jogada) % (m+1) == 0:
            print("O computador tirou",jogada,"peças.")
            return jogada
        else: 
            jogada = jogada - 1

def jogada_invalida():
    print ("Oops! Jogada inválida! Tente novamete!")

def campeonato():
    aux = 1
    vitoria_computador = 0 
    vitoria_usuario = 0
    while aux <= 3:
        print("**** RODADA",aux,"****")
        SuaJogada = partida()
        if SuaJogada:
            vitoria_usuario = vitoria_usuario + 1
        else: 
            vitoria_computador = vitoria_computador + 1
        aux = aux + 1
    print("Fim de campeonato!")
    print("Placar: Você",vitoria_usuario,"X",vitoria_computador,"Computador")

print("Bem-vindo ao jogo NIM!!! Escolha:")
print("1 - para uma partida isolada")
tipo = int(input("2 - para um campeonato"))
if tipo == 1:
    print("Você escolheu uma partida!!")
    partida()
else:
    print("Você escolheu um campeonato!!")
    campeonato()




