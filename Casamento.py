#Programa
#Subprogramas
def listaCasaveis(nmCli, prefsCli, qtd, nmCadastro):
    #Impressões que associam o cliente com os do arquivo.
    print("listagem dos Casáveis com", nmCli)
    print("Quantidade Mínima de Preferências em Comum", qtd)
    # Arquivo é aberto
    dados = open(nmCadastro, "r", encoding="utf-8")
    # Leitura do arquivo linha a linha.
    for linha in dados:
        # Para cada leitura, pega cada palavra da linha e coloca numa lista
        infos = linha.strip("\n").split("#")
        # O nome será a primeira informação
        nomeCandidato = infos[0]
        # A informação das preferências é a partir da segunda palavra, formamos um conjunto delas
        prefsCandidato = set(info[1:])
        # Aqui é feita a interseção do conjunto das preferências do cliente com a pessoa da linha
        prefsComuns = prefsCli.intersection(prefsCandidato)
        # Se a quantidade de itens da interseção for maior ou igual a quantia que eu queria no inicio, é printado o nome da pessoa.
        if len(prefsComuns) >= qtd:
            print(nomeCandidato)
    # O arquivo é fechado
    dados.close()
    print()
    return None

#Principal
# Nome do cliente
nomeCliente = input()
# Conjunto de preferência da pessoa
preferenciasCliente = set(input().split("#"))
# Quantas quantidades em comum eu quero que tenha do cliente com o pessoal do arquivo.
qtdComuns = int(input())
# Nome do arquivo.
nomeCadastrados = input()
# Função que pega todas as informações, que do arquivo de pessoas mostram as que tem as preferências ( de acordo com a quantia)
listaCasaveis(nomeCliente, preferenciasCliente, qtdComuns, nomeCadastrados)
