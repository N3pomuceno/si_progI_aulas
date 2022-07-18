#entradas múltiplas
#185 75.5 28

#primeira forma de fazer

entradas = input().split()
#esse spli faz o separador ser o espaço em branco, ou o caractér que estiver entre parênteses com aspas
#poderia ser split("#") e o # seria o separador entre os dados

#colocar mais ou menos valores entradas dará erro no input

#se não colocássemos int ou float antes das entradas, as 3 variáveis altura peso e idade seriam strings
altura = int(entradas[0])   #a primeira entrada está associada com o [0], com a lista de input feita
peso = float(entradas[1])   #A segunda entrada está associada com o [1]
idade = int(entradas[2])    #a terceira entrada está associada com o [2]



#podemos fazer de outra formas esse mesmo cálculo
#map, função de segunda ordem para entradas múltiplas, ele é só para ajudar a gente,
# para converter as variáveis na primeira parte do comando para as variáveis da lista da segunda parte

"""
altura, peso, idade = map(float, input().split())
altura= int(altura)
idade = int(altura)
print(altura, peso, idade)
"""