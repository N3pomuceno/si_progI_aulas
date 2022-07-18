#pelo menos uma lista de 5 valores
#map é um objeto, tem características associadas, se colocar o map direto da segunda linha, terá erro, ele não é um
# comando para converter, transformando em lista é possível.
#MAP é convertível

valores = input().split()
valores = list(map(float, valores))
print(valores)
a,b,c = valores[3:5]    #ele admite para a b c pela ordem dos valores colocados de 3 a 5
print(a,b,c)

'''podemos definir diretamente as variáveis 
da seguinte forma 
a,b,c = list(map('conversor'(),input().split())) TENDO QUE COLOCAR O NUMERO DE DADOS IGUAL AO NUMERO DE VARIAVEIS
podendo separar para deixar mais simples.

'''