#perimetro do círculo
PI = 3.14159    #constante definida
raioString = input()    #dado em string do raio, agora precisa transformar em float para fazer o cálculo
raio = float(raioString)    #raio é o dado do raio em float
perimetro = 2 * PI * raio   #cálculo do perimetro
print("%4.1f"%perimetro)    #o primeiro dígito depois do % descreve a quantidade de caractéres que terá na resposta

#depois do ponto está relacionado com a quantidade de casas decimais, o f define a tipo de caracter, no caso é float

#e depois do segundo % vc explicita a variável


