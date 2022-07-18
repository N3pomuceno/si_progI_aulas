# Programa - Conjunto de palavras com vários caractéres.
# Subprogramas
def produz(nm):
    conjPals = set() #se colocar {} também serve, mas pode ser dicionário tbm.
    # Abre arquivo
    dados = open(nm, "r", encoding="utf-8")
    # Iteração que passa de linha a linha, pegando frases.
    for linha in dados:
        # Todas as palavras da frase entram numa lista que tiram o \n e separam os espaços.
        pals = linha.strip("\n").split()
        # E para cada palavra dessa lista, é adicionado no conjunto, repetições o conjunto tira
        for p in pals:
            conjPals.add(p)
    # Fecha o arquivo.
    dados.close()
    return conjPals

def mostrar(conjunto):
    print("Conjunto:")
    # Para cada item do conjunto - NOTA QUE O SORTED TRANSFORMA O CONJUNTO EM LISTA ORDENADA
    for item in sorted(conjunto):
        # Impressão do item
        print(item)
    print()
    return None

def produzCaracteres(conjPals):
    # Cria um conjunto
    conjCaracs = set()
    # Iteração que passa em cada palavra do conjunto.
    for pal in conjPals:
        # Iteração que passa em cada caracter do conjunto
        for c in pal:
            # Adiciona o caracter no conjunto de caracteres, repetição de caracter não coloca.
            conjCaracs.add(c)
    return conjCaracs

#Para ter uma noção de ordem teria que transformar numa lista ou usar o sorted. O sorted transforma o conjunto numa lista! E o ordena.

# Principais
# Nome do arquivo
nome = input()
# função que cria um conjunto e adiciona todas as palavras do arquivo
conjPalavras = produz(nome)
# Impressão do conjunto
print(conjPalavras)
# Função de impressão do conjunto
mostrar(conjPalavras)
# Função que pega do conjunto de palavras e cria um conjunto de letras em cima dele.
conjCaracteres = produzCaracteres(conjPalavras)
# Função de impressão do conjunto
mostrar(conjCaracteres)
