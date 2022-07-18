"""
O que é isso?


"""


#Programa
#Subprograma
#Subprograma que retona a soma de dois números.
def incrementa(q,passo):
    return q + passo

def incrementa2(pars, passo):
    pars[0] += passo
    return None

#Principal
qtd = 0
print(qtd)
qtd = incrementa(qtd, 3)
print(qtd)

parametros = [0]
print(parametros)
incrementa2(parametros, 3)
print(parametros)
