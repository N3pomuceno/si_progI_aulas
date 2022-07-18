#lógica, acredito que falta conhecimento para fazer isso.
#Mas para mim, eu usaria o while para definir uma condição para manter enquanto não estiver ordenado.

# criaria uma variável de apoio para conseguir fazer a troca de posição da lista da variáveis.

#PRECISA SABER CRIAR VETOR.

def ordem(vet):
    #Aqui podemos fazer a referência tanto pela posição quanto pelo valor em si. e podemos criar um vetor de saída ou trabalhar com o próprio vet
    #Usaremos o vet para tentar diminuir o custo do programa
    for pos in range(len(vet)):
        for var in range(pos, len(vet)):  #Nessa ideia aqui, ela naturalmente fará mais passos que o se eu fizesse um subprograma que definiria qual é a posição ou o menor valor do vetor de uma vez só
            if vet[pos] > vet[var]:       #Seria mais otimizado fazer um subprograma com a função só de ler, e encontrar a menor posição, farei isso no segundo programa
                temp = vet[var]           #Tendo em vista isso, um pensamento extra, caso a gente faça o cálculo, esse if pode trabalhar até len(vet) - 1 vezes só numa repetição.
                vet[var] = vet[pos]
                vet[pos] = temp

    return vet

def escrever(num):
    vet = []
    for ind in range(num):
        n = int(input())
        vet.append(n)
    return vet

def mostrar(vet):
    for j in range(len(vet)):
        print("{}".format(vet[j]))
    print()
    return None

#Fazendo de duas formas para fazer esse cálculo, pode ser pela linha ou a cada enter, vou começar pelo segundo e depois vou fazer por linha.
#Ao mesmo tempo tem a possibilidade de fazer com um while que define a quantidade de valores na hora. ou definir de antemão qual é a quantidade de valores, vamos começar com o segundo também.

qtd = int(input("Quantidade de valores no vetor:"))
vetor = escrever(qtd)
vetorOrdenado = ordem(vetor)
mostrar(vetorOrdenado)


