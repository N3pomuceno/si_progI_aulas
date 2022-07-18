#Leia números inteiros da entrada padrão até que um número negativo
# seja digitado. Para cada número lido, exceto para o negativo, escreva na saída padrão
#se aquele número é primo ou não.

#Definição: um número inteiro é primo se e somente se for maior que um e for apensar divisível por ele mesmo.

#programa Primos ou não

#Subprogramas
def processa(num)
    divisor = 2
    while divisor <= num//2 and num % divisor != 0:
        dividor += 1
    if num > 1 and dividor > num//2:
        print(num, "é primo")
    else:
        print(num, "não é primo")
    return None


# tem outras formas de fazer esse cálculo, qual é o custo computacional para fazer isso? Temos que fazer o menor trabalho possível
#falo isso pensando na linha 12 e 14, nas condições, que ao invés de pegar metade do número, pode ser só trabalhar com a raiz do número +1.

#Principal
entradaLida = int(input()) #pega primeiro
while entradaLida >= 0:
    processa(entradaLida)
    entradaLida = int(input()) #Pega o próximo