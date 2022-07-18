# Programa Editor de Arquivo texto
# TODO estudar
# Subprogramas
def menu(listaOps):
    for op in listaOps:
        print(op)
    return int(input("Escolha:\> "))

def mostrarArquivo(nome):
    dados = open(nome, "r", encoding="utf-8")
    print("Conteúdo do arquivo",nome)
    """
    linha = dados.readline()
    while linha != "":
        print(linha, end="")
        linha = dados.readline()   - Ele não quer que utilize readlineS, com s, ocupa espaço da memória de forma desnecessária
        Para cada novo readline usado sobre o mesmo arquivo ele pula para a próxima linha referente ao último que ele tinha chegado
    """
    for linha in dados:
        print(linha, end="")
    dados.close()
    print()
    return None

def criarArquivo(nome):
    #Definir o nome do arquivo aqui, se eu quiser mudar o tipo do arquivo, basta escrever .py ou o que eu quiser para definir a extensão do arquivo.
    dados = open(nome, "w", encoding="utf-8")
    dados.close()
    return None

def destruirArquivo(nome):
    from os import remove #Comando do sistema operacional de remover arquivo, muito poder.
    remove(nome)
    return None

def anexarLinhaEmArquivo(nome):
    linhaNova = input()
    dados = open(nome, "a", encoding="utf-8")
    dados.write(linhaNova+"\n") #Quando der o write, tem que sempre dar o \n para pular a linha, pois isso é filtrado quando é escrito
    dados.close()
    return None

def inserirNovaLinhaEmPosicao(nome):
    from os import remove, rename
    novaLinha = input()
    posicao = int(input())
    dados = open(nome, "r", encoding="utf-8")
    temporario = open(nome+"$$$", "w", encoding="utf-8")
    posAtual = 0
    for linha in dados:
        posAtual += 1
        if posicao == posAtual:
            temporario.write(novaLinha+"\n")
        temporario.write(linha)
    if posicao > posAtual:
        temporario.write(novaLinha+"\n")
    temporario.close()
    dados.close()
    remove(nome)
    rename(nome+"$$$", nome)
    return None

def removerLinhaEmPosicao(nome):
    from os import remove, rename
    posicao = int(input())
    dados = open(nome, "r", encoding="utf-8")
    temporario = open(nome+"$$$", "w", encoding="utf-8")
    posicaoAtual = 0
    for linha in dados:
        posicaoAtual += 1
        if posicao != posicaoAtual:
            temporario.write(linha)
    if posicao > posicaoAtual:
        print("Erro - linha inesxistente!!!")
    temporario.close()
    dados.close()
    remove(nome)
    rename(nome+"$$$", nome)
    return None
# principal

OPS = ["(0) Conectar", "(1) Mostrar","(2) Criar","(3) Destruir","(4) Anexar linha ao fim",
    "(5) Inserir linha nova em Posição","(6) Remover linha em Posição","(9) Sair"]
nomeArquivo = "default.txt"
criarArquivo(nomeArquivo)
opcao = menu(OPS)
while opcao != 9:
    if opcao == 0:
        nomeArquivo = input()
    elif opcao == 1:
        mostrarArquivo(nomeArquivo)
    elif opcao == 2:
        criarArquivo(nomeArquivo)
    elif opcao == 3:
        destruirArquivo(nomeArquivo)
    elif opcao == 4:
        anexarLinhaEmArquivo(nomeArquivo)
    elif opcao == 5:
        inserirNovaLinhaEmPosicao(nomeArquivo)
    elif opcao == 6:
        removerLinhaEmPosicao(nomeArquivo)
    opcao = menu(OPS)
