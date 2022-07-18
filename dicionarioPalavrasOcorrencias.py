# Programa
# Subprogramas
def produz(nm):
    # Cria um arquivo de dicionário
    dicionarioPsOcs = dict()  # ou {} dicionario inicializado
    # Abrindo o arquivo
    dados = open(nm, "r", encoding="utf-8")
    # Leitura das linhas
    for linha in dados:
        # Lista de palavras, separando por espaços, e tirando o \n
        palavras = linha.strip("\n").split()
        # Iteração para passar em cada uma das palavras para adicionar na palavras
        for p in palavras:
            # Seleção de se a palavra já está no dicionário ou não.
            if dicionarioPsOcs.get(p) == None: #OUTRA FORMA: if p not in dicinarioPsOcs:
                # Se não estiver coloque uma nova chave com o nome da palavra e coloque o contador 1
                dicionarioPsOcs[p] = 1
            else:
                # Se já estiver, adicione mais um ao número relacionado a (chave) palavra.
                dicionarioPsOcs[p] += 1
    # Fechamento do arquivo
    dados.close()
    return dicionarioPsOcs

def mostrar(dicionarioPsOcs):
    print("Conteúdo do Dicionário:")

    #FORMA ALTERNATIVA:
    #for chave in dicionarioPsOcs:
    #    print(chave, dicionarioPsOcs[chave])

    for chave, valor in dicionarioPsOcs.items():
        print("\t%13s %2d"%(chave+" "*(13 - len(chave)), valor))
    print()
    return None

# Principal
# Nome do Arquivo
nome = input()
# Função que com o nome do arquivo, retorna o dicionário do arquivo
dicionarioPalavrasOcorrencias = produz(nome)
# Função de impressão do dicionário
mostrar(dicionarioPalavrasOcorrencias)
