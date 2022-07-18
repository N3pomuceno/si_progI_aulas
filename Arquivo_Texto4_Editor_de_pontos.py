#Programas
# TODO estudar
#Subprogramas
def menu(opcoes):
    print("----- Menu de Opções -----")
    for op in opcoes:
        print(op)
    return int(input("Escolha: "))

def gerarAleatorio(nm, qt, min, max):
    from random import randint
    dados = open(nm, "w")
    for i in range(qt):
        x = randint(min, max)
        y = randint(min, max)
        dados.write(str(x)+" "+str(y)+"\n")
    dados.close()
    return None

def mostra(nm):
    print(nm+":")
    dados = open(nm, "r")
    for linha in dados:
        print(linha, end="")
    dados.close()
    print()
    return None

def criar(nm):
    dados = open(nm, "w")
    dados.close()
    return None

def distancia(xA, yA, xB, yB):
    return((xB - xA)**2+(yB - yA)**2)**0.5

def achaMaisProximo(xVc, yVc, nm):
    dados = open(nm, "r")
    linha = dados.readline()
    if linha == "":
        xMProx = yMProx = dMProx = None
    else:
        xMProx, yMProx = map(int, linha.split())
        dMProx = distancia(xVc, yVc, xMProx, yMProx)
        for linha in dados:
            xAtual, yAtual = map(int, linha.split())
            dAtual = distancia(xVc, yVc, xAtual, yAtual)
            if dAtual <dMProx:
                dMProx = dAtual
                xMProx, yMProx = xAtual, yAtual
    dados.close()
    return xMProx, yMProx, dMProx

def maiorDistancia(x, y, nm):
    dados = open(nm, "r")
    linha = dados.readline()
    if linha == "":
        xMD = yMD = None
        dist = 0
    else:
        xMD, yMD = map(int, linha.split())
        dist = distancia(x, y, xMD, yMD)
        for linha in dados:
            xAtual, yAtual = map(int, linha.split())
            distAtual = distancia(x, y, xAtual, yAtual)
            if distAtual >  dist:
                dist = distAtual
                xMD, yMD = xAtual, yAtual
    dados.close()
    return xMD, yMD, dist

def maisDistantesEntreSi(nm):
    dados = open(nm, "r")
    linha = dados.readline()
    if linha == "":
        xA = yA = xB = yB = distAB = None
    else:
        xA, yA = map(int, linha.split())
        xB, yB, distAB = maiorDistancia(xA, yA, nm)
        for linha in dados:
            xAAtual, yAAtual = map(int, linha.split())
            xBAtual, yBAtual, distAtual = maiorDistancia(xAAtual, yAAtual, nm)
            if distAtual > distAB:
                distAB = distAtual
                xA, yA, xB, yB = xAAtual, yAAtual, xBAtual, yBAtual
    dados.close()
    return xA, yA, xB, yB, distAB

#Principal

OPS = ["(0) Escolher nome do Arquivo", "(1) Criar Arquivo de Pontos", "(2) Mostrar", "(3) Ponto mais próximo de você",
       "(4) O ponto mais distante de você", "(5) Os dois pontos mais distantes", "(6) Sair"]
opcao = menu(OPS)
nomeDoArquivo = "defaultPts.txt"
while opcao != 6:
    if opcao == 0:
        nomeDoArquivo = input("Novo nome do arquivo: ")
        criar(nomeDoArquivo)
    elif opcao == 1:
        qtdPontos, minimo, maximo = map(int, input("Qtd, Min e Max: ").split())
        gerarAleatorio(nomeDoArquivo, qtdPontos, minimo, maximo)
    elif opcao == 2:
        mostra(nomeDoArquivo)
    elif opcao == 3:
        xVoce, yVoce = map(int, input("Diga sua posição: ").split())
        xMaisProximo, yMaisProximo, distMaisProximo = achaMaisProximo(xVoce, yVoce, nomeDoArquivo)
        print("O ponto mais próximo de (%d,%d) é: (%d,%d), com distância: %.1f"%
              (xVoce, yVoce, xMaisProximo, yMaisProximo, distMaisProximo))
    elif opcao == 5:
        xA, yA, xB, yB, distaciaAB = maisDistantesEntreSi(nomeDoArquivo)
        print("(%d, %d) e (%d, %d) são os mais distantes entre si com distância de : %.1f"%(xA, yA, xB,yB, distaciaAB))
    opcao = menu(OPS)
