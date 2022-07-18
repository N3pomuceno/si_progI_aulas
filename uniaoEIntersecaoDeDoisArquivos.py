# Programa
#Subprogramas
def produz(nm):
    conjPals = set() #se colocar {} também serve, mas pode ser dicionário tbm.
    dados = open(nm, "r", encoding="utf-8")
    for linha in dados:
        pals = linha.strip("\n").split()
        for p in pals:
            conjPals.add(p)
    dados.close()
    return conjPals

def mostrar(conjunto, msg):
    print("Conjunto: {}".format(msg))
    for item in sorted(conjunto):
        print(item)
    print()
    return None

#Principal
# Nome dos dois arquivos no qual eu quero fazer a operação de união e de interseção
nomeA, nomeB = input().split()
# Chama a função que pega todas as palavras dos dois arquivos e transforma em conjuntos
conjuntoA = produz(nomeA)
conjuntoB = produz(nomeB)
# Impressão dos conjuntos
mostrar(conjuntoA, nomeA)
mostrar(conjuntoB, nomeB)
# É feito a interseção dos dois conjuntos, e depois sua impressão
intersecaoAB = conjuntoA.intersection(conjuntoB)
mostrar(intersecaoAB, "Interseção {} com {}".format(nomeA, nomeB))
# É feito a união dos dois conjuntos, e depois sua impressão
uniaoAB = conjuntoA.union(conjuntoB)
mostrar(uniaoAB, "União {} com {}".format(nomeA, nomeB))
