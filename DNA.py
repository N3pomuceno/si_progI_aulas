"""
Leia da entrada padrão a quantidade de nuclídeos de uma pessoa.
Gere aleatoriamente o DNA deta pessoa.
Em seguida, leia o DNA de uma doença.
Em seguida, leia a quantidade mínima de ocorrências do DNA da doença na pessoa para afirmar
que ela possua ou não esta tal doença.

Teste:
Entradas:
34
ACGA
3

Saídas Correspondentes:
Pessoa: CTAGCTAGCATCGATGCTACGATCGTTGACTGATCG
Doença:ACGA
Análise: Pessoa não possui essa doença.

"""

#Programa
#Subprograma
def geraDNA(qtd):
    #O seguinte comando é de pegar na biblioteca de RANDOM o comando de randint, que é gerar um inteiro (definindo um máximo e um mínimo)
    from random import randint
    #Definimos uma constante que pega todas as possibilidades de elementos que um dna pode ter, e coloca junto, que dele nós vamos sortear.
    #Partimos de uma variável que parte de nenhum termo "", para depois fzer uma iteração, um laço que vai trazer todos os elementos de acordo com a quantidade que decidimos inicialmente.
    BASES = "ACTG"
    dna = ""
    #Aqui está a iteração que trazerá o dna, ela repete de acordo com a quantidade que escolhemos para a pessoa.
    for i in range(qtd):
        # repare que a variável dna é concatenada toda vez que repete o loop, e esse randint ele está pegando uma das 4 posições que é composta por BASES e colocando no DNA, sendo que de 0 a 3, temos A C T G respectivamente
        dna += BASES[randint(0,3)]
    return dna

def analise(dnaP,dnaD,qtdMin):
    #A ideia dessa função é que a pessoa não terá a doença até que a contagem de quantidade mínima de aparições do genoma seja satisfeita. Por isso resposta começa recebendo esse valor.
    resposta = "Pessoa não possui esta doença"
#    if dnaP.count(dnaD) >= qtdMin: Não pode usar esse comando, mas esse count mostra a quantidade de dnaD em dnaP é isso
#        resposta = "Pessoa possui a doença"
    #Daqui temos que iniciar do zero pois ela vai sendo acrescentada a cada loop.
    contagem = 0
    #Aqui está a repetição que se repete de acordo com o tamanho do dna da pessoa, pois assim pode começar de cada um dos pontos e fazer a comparação com o comando Se para ver se tem o dna da doença
    for i in range(len(dnaP)):
        #Esse if pega  do i-esimo endereço do dna da pessoa até o espaço do mesmo tamanho do dna da doença para fazer a comparação, caso apareça soma na contagem caso contrário a iteração continua.
        if dnaP[i:i+len(dnaD)] == dnaD:
            contagem += 1
    #Por fim, se a quantidade de vezes que o dna da doença aparece no dna da pessoa for maior que a quantidade de contagem mínima, vc altera o valor da resposta para dizer que a pessoa tem a doença.
    if contagem >= qtdMin:
        resposta = "Pessoa possui a doença"
    return resposta

#Principal
#Inicialmente temos que definir o tamanho do DNA da pessoa, e a sequência genética da doença para randomizar o dna da pessoa e verificar se existe a sequencia da doença na pessoa
#Depois temos que definir a quantidade de vezes que a sequência genética da doença tem que aparecer no DNA para.
qtdDNAPessoa = int(input())
dnaDoenca = input()
qtdMinimaOcorrencias = int(input())
#A função geraDNA cria de forma randomica o padrão para o DNA da pessoa
dnaPessoa = geraDNA(qtdDNAPessoa)
print("Pessoa:", dnaPessoa)
print("Doença:", dnaDoenca)
#Esse print seguinte mostra o resultado da função analise, que retorna algum dado. Mais especificamente o resultado da pessoa se ela tem a doença ou não.
print(analise(dnaPessoa, dnaDoenca, qtdMinimaOcorrencias))
