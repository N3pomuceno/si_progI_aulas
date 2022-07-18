"""
MESMA COISA SÓ QUE FAZENDO DE UMA OUTRA FORMA:
Leia números da entrada padrão até que um número negativo seja digitado NUMA LINHA.
Identifique qual o maior número lido e quantos doram os números lidos,
O número negativo não deve ser contado.

Teste 1
Entradas:
1432
842.2354
47327
434
-1

Saída correspondente:
Maior número lido: 47327.0
Quantidade de números lidos: 4

Teste 2
-1
Saída correspondente:
Nenhum número válido foi lido!!!

"""
#Programa Maior lido e quantos
#Subprogramas
def maiorNumero(vals):
    maior = vals[0]
    for i in range(1,len(vals)):
        if vals[i] > maior:
            maior = vals[i]
    return maior


#Principal
valores = list(map(float, input().split()))
if valores ==[]
    print("Nenhum Número Foi Lido!!!")
else:
    print("Maior Número Lido:", maiorNumero(valores))

"""
Explicando então o que está acontecendo nesse programa
o programa principal é simples, o valores pega os números colocados em uma linha e coloca numa lista da forma de float.
então é usado o comando de seleção if, que se o valores for vazio, caso valores == [], ele printa que nenhum número foi
lido, e depois caso contrário ele mostra o maior número lido baseado no subprograma chamado maiorNumero.

Então é usado o for para fazer a comparação de todos os número da lista horizontal, e depois  o maior só pega o
maior valor de todos.
O interessante é que pela definição do for, eu só poderia colocar o vals como lista que o for passaria por todos os 
valores da lista, e a comparação do if seria o próprio i com o maior.

 
"""

