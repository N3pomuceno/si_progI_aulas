#Programa

#Subprogramas
def geraAleatoria(qL, qC, min, max):
    #Pegando da biblioteca random o comando de randint
    from random import randint
    #A matriz inicia de uma lista vazia:
    vals = []
    #E parte de dois comando de repetições para fazer a matriz: O primeiro para definir a quantidade de linhas, pois é como se fosse cada lista dentro da lista/matriz fosse uma linha, e assim a quantidade de listas está associado a quantidade de linhas.
    for lin in range(qL):
        # O primeiro passo é criar uma lista que será a linha em questão.
        novaLinha = []
        #E daí fazer a segunda repetição que será o que define a quantidade de colunas, quantos elementos terão em cada linha, em outras palavras, serão as quantidade de colunas.
        for col in range(qC):
            #É gerado um valor que é adicionado na linha através do append
            novoValor = randint(min, max)
            novaLinha.append(novoValor)
        #Depois essa linha que foi gerada de forma randomica é adicionada na primeira lista que se tornará a matriz
        vals.append(novaLinha)
    return vals

def mostra(vals):
    #Função para mostrar a matriz, com duas repetições, a primeira pega cada uma das listas, uma por uma:
    for linhaDeValores in vals:
        #Em seguida pega valor a valor e print eles com a formatação de 4d, 4 caractéreis no formato de inteiro, pois no máximo cada um deles podem ter 3 caractéres, exemplo -10, e para ficar visualmente agradável a gente adiciona mais um. além disso tem aquele final de end="" para que a linha não seja pulada no final pois se não houvesse teria como normalidade aquele \n que pula linha;
        for valor in linhaDeValores:
            print("%4d" % valor, end="")  #Forma de colocar as coisas na linha de uma vez só, o primeiro print vazio e para pular para a linha de baixo e não continuar mostrando seus valores na sequência, o segundo print vazio é para pular a linha depois da matriz por questão de organização/formatação
        print()
    print()
    return None


def somar(pos, vals, alcance):
    #Inicialmente vou deixar claro que começamos a soma de um valor diferente de zero pois não queremos contar o valor da própria posição, então fazemos a soma de todas os valores inclusive a própria posição, contudo inicialmente já temos o valor da posição negativo para que seja cortado.
    soma = -vals[pos[0]][pos[1]]
    #Aqui começa as duas iterações para que seja possível fazer a soma dos valores, repare que o range, para as linhas começa do valor da posição menos o alcance que queremos, até a posição mais o alcance mais um, esse mais um é devido a como o range interage que pega o valor -1. A segunda iteração é para as colunas.
    for lin in range(pos[0] - alcance, pos[0] + alcance + 1):
        for col in range(pos[1] - alcance, pos[1] +alcance + 1):
            #Esse if é para que os limites da matriz não sejam ultrapassados, pois isso verifica se os casos estão nas linhas e nas colunas da matriz, caso isso aconteca, ele soma o valor, caso contrário nada acontece.
            if 0 <= lin < len(vals) and 0 <= col < len(vals[0]):
                soma += vals[lin][col]
    return soma

def localizaPosicao(vals, alcance):
    #Começa a localização baseada num palpite para começar a trabalhar (endereço no formato de tupla)
    posicao = (0, 0)
    #Temos que tbm já definir o valor da soma da posição do palpite para poder comparar com os outros, então chamamos a função somar, que pega a posição, a matriz, e o alcance que deve ser somado.
    maiorSoma = somar(posicao, vals, alcance)
    #Depois de definir tudo que é necessário sobre o palpite inicial teremos que comparar com cada um das possíveis posições, então como estamos trabalhando em uma matriz precisamos fazer duas repetições de acordo com a quantidade de linhas e com a quantidade de colunas.
    for lin in range(len(vals)):
        for col in range(len(vals[lin])):
            #É definido a posição da matriz de acordo com os índices das repetições que são de acordo com a qtd de linhas e colunas. Definimos a posição e a soma tbm para que possa ser comparado com a posição do palpite com o comando se
            posicaoAtual = (lin, col)
            somaAtual = somar(posicaoAtual, vals, alcance)
            #Aqui está a comparação, caso a posição atual tenha sua soma maior que a soma da posição do palpite, o valor do palpite é atualizado e assim vai percorrendo da a matriz.
            if somaAtual > maiorSoma:
                maiorSoma = somaAtual
                posicao = posicaoAtual
    return posicao, maiorSoma


#Principal
#Valores é uma matriz que vai ser criada sendo chamado uma função que precisa de 4 parâmetros, linha, coluna, valor mínimo e máximo.
valores = geraAleatoria(3, 5, -10, 10)
#Aqui basicamente é uma função só para mostrar explicitamente a matriz que foi formada.
mostra(valores)
#No seguinte passo é feito uma função que retorna a posição na matriz que a soma dos seus vizinhos (de alcance definido) é a maior dentre todas.
posicaoCelulaDeMaiorSomaDeVizinhaca = localizaPosicao(valores, 1)
print(posicaoCelulaDeMaiorSomaDeVizinhaca)
