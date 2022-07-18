#Programa
#TODO estudar
#Subprogramas
def mostrar(nm):
    print(nm+":")
    dados = open(nm, "r")
    for produto in dados:
        print(produto, end="")
    dados.close()
    print()
    return None

def insereOrdenado(nm, c, q, p):
    from os import remove, rename
    dados = open(nm, "r")
    temporario = open(nm+"$$$", "w")
    naoInseri = True
    for produto in dados:
        cod, qtd, pre = produto.split()
        qtd = int(qtd)
        pre = float(pre)
        if c== cod:
            novoPreco = (p*q + pre*qtd)/(q + qtd)
            temporario.write(cod+" "+str(q+qtd)+" "+"%.2f"%novoPreco+"\n")
            naoInseri = False
        else:
            if naoInseri and c < cod:
                temporario.write(c+" "+str(q)+" "+str(p)+"\n")
                naoInseri = False
            temporario.write(produto)
    if naoInseri:
        temporario.write(c + " " + str(q) + " " + str(p) + "\n")
    dados.close()
    temporario.close()
    remove(nm)
    rename(nm+"$$$", nm)
    return None

def balanco(nmS,nmC):
    dadosC = open(nmC, "r")
    for produto in dadosC:
        codigo, qtd, preco = produto.split()
        qtd = int(qtd)
        preco = float(preco)
        insereOrdenado(nmS, codigo, qtd, preco)
    dadosC.close()
    return None

#Principal
nomeSupermercado, nomeDoCaminhao = input().split()
mostrar(nomeSupermercado)
mostrar(nomeDoCaminhao)
balanco(nomeSupermercado, nomeDoCaminhao)
mostrar(nomeSupermercado)

