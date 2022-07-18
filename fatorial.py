# TODO estudar
#Refazer com recursividade, rever vídeo aulas de recursividade

def fat(num, resultado):
    if resultado == []:
        resultado.append(num)
    else:
        resultado[0] = resultado[0]*num
    if num == 1:
        print(resultado)
        return None
    elif num == 0:
        resultado[0] = 1
        print(resultado)
        return None
    return fat(num - 1, resultado)

numero = int(input())
lista = []
fat(numero, lista)
