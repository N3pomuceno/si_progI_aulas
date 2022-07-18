linha = input()
while linha != "2":
    if linha == "1":
        linha = input()
    golsG, golsI = map(int, linha.split())
    print(golsG,golsI)
    linha = input()

"""
programa comentado da aula do professor,
Problema dos jogos de futebol Uri 1131

O interessante desse código é que o professor em todo o momento só utilizou de uma variável, de um espaço que está 
constantemente mudando de acordo com o que ele quer. 

DÚVIDA: um custo de um algoritmo é baseado de acordo com a quantidade de repetição, contudo o número de variáveis 
tbm irá afetar na quantidade do custo?

Inicialmente a linha está na forma de string, somente quando definindo gols que ele coloca na forma de inteiro 
na linha 5, com o objeto map. DÚVIDA: Nao precisaria de list?

O mesmo espaço usado para ver se é para continuar lendo, ele usa para colocar o placar dos jogos.


"""