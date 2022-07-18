#Programa  Agrupa Pontos do Espaço 2D
#Desisti de copiar no meio, talvez perguntar al´guem se copiou o arquivo
#Tirei alguns prints da aula, mas não são de todas as partes
#Subprogramas
def mostrar(nm):
    dados = open(nm, "r")
    print(nm+":")
    x, y = tuple(map(int, dados.readline().split()))
    while (x, y) != (0, 0):
        print("\t", (x, y))   #\t é para a tabulação
        x, y = tuple(map(int, dados.readline().split()))
    dados.close()
    print()
    return None

def centroide(g):
    somaX = somaY = 0
    for x, y in g:
        somaX += x
        somaY += y
    return somaX/len(g), somaY/len(g)


def distancia(xP, yP, grupo):
    if grupo == None:
        return 0
    else:
        xCentroide, yCentroide = centroide(grupo)
        return ((xCentroide - xP)**2 + (yCentroide - yP)**2)**0.5

def achaGrupoMaisProximo(xPt, yPt, qG lisGs):
    posVencedor = 0
    distVencedor = distancia(xPt, yPt, nmPts+"G0")
    for pos in range(1, len(lisGs)):
        distAtual = distancia(xPt, yPt, lisGs[pos])
        if distAtual < distVencedor:
            distVencedor = distAtual
            posVencedor = pos
    return posVencedor

def criarArquivo(nm):
    dados = open(nm, "w")
    dados.close()
    return None

def anexa(xP, yP, nm):
    dados = open(nm, "a")
    dados.write(str(xP)+" "+str(yP)+"\n")
    dados.close()
    return None

def agrupa(qGs, nmPts):
    #listaGs = [None]*(qGs), deixando isso de lado e fazendo com arquivos:
    for i in range(qGs):
        criarArquivo(nmPts+"G"+str(i))
    dados = open(nmPts, "r")
    x, y = tuple(map(int, dados.readline().split()))
    while (x, y) != (0, 0):
        posGrupo = achaGrupoMaisProximo(x, y, qGs, nmPts)
        anexa(x, y, nmPts+"G"+str(posGrupo))
        x, y = tuple(map(int, dados.readline().split()))
    dados.close()
    return listaGs

def mostrarGps(qGs, nmPts):
    print("Grupos:")
    for g in range(qGs):
        dados = open(nmPts+"G"+"g", "r")
        for
        print("\t", g)
    print()
    return None

#Principal
nomeArqPontos = input()
qtdGrupos = int(input())
mostrar(nomeArqPontos)
grupos = agrupa(qtdGrupos, nomeArqPontos)
mostrarGps(qtdGrupos, nomeArqPontos)
