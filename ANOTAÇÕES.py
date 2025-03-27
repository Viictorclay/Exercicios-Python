
#int = NUMERO INTERIO (3)
#float = NUMERO REAL (5.5)
#bool = True or False (VERDADEIRO ou FALSO)
#str = "Olá" & "7,5" (TUDO QUE É CONSIDERADO ESCRITA)

#-------------------------------------------------------------

print("Olá, Usuario !")
nome = input("Como se chama? ")
print("Seja Bem-vindo(a)", nome)
dia = input("Em que dia você nasceu? ")
mes = input("Em que mês? ")
ano = input("Em que ano? ")
print(nome, "nasceu no dia", dia ,"de", mes , "de", ano,".")
print("agora, vamos fazer uma soma simples,", nome)
n1 = int(input("Digite um numero. "))
n2 = int(input("Agora, Digite outro numero. "))
s = n1 + n2

#print(n1 ,"+", n2 , "é igual a", int(n1)+int(n2))
#                 (METODO ANTIGO)
#print("A soma entre {} e {} vale {}".format(n1, n2, s))

print(f"A soma entre {n1} e {n2} é {s}") #f = .format

#-------------------------------------------------------------

n = input("Digite: ")
print(n)
print(f"Só tem espaços?{n.isspace()}") #.isspace   SÓ ESPAÇO
print(f"È numerorico?{n.isnumeric()}") #.isnumeric NUMERO
print(f"È alfabetico?{n.isalpha()}") #.isalpha     LETRAS
print(f"È Alfanumerico?{n.isalnum()}") #.isalnum  NUMERO&LETRA
print(f"Está em letras MAIÚSCULAS?{n.isupper()}") #.isupper
print(f"Está em letras minúsculas?{n.islower()}") #.islower
print(f"Está capitalizada?{n.istitle()}") #.istitle Power

#-------------------------------------------------------------

nome = input("Qual é seu nome? ")
print(f"Prazer em te conhecer {nome:^20}!") # :^20 Centralização da vareavel

n2 = int(input("Digite outro numero. "))
s = n1 + n2  # SOMA
m = n1 * n2  # MULTIPLICAÇÃO
d = n1 / n2  # DIVISÃO
di = n1 // n2  # DIVISÃO INTEIRA
e = n1 ** n2 # EXPOENENCIAÇÃO
print(f"O resultado da some é {s:-> 22}")
print(f"O resultado da multiplicação é {m:-> 13}")
print(f"O resultado da divisão é {d:-> 20}")
print(f"O resultado da divisão interia é {di:-> 10}")
print(f"O resultado da exponenciação é {e:-> 15}")

#-------------------------------------------------------------

import math   # BIBLIOTECA MATEMATICA

num = float(input("Digite um numero: "))
arredondarCIMA = math.ceil(num)  # ARREDONDADER PRA CIMA
arredondarBAIXO = math.floor(num)  # ARREDONDADER PARA BAIXO
partINTERIA = math.trunc(num)  # SÓ A PARTE ANTES DA VIRGULA
potencia = math.pow(num)  # POTENCIA 
raizQ = math.sqrt(num)  # RAIZ QUADRADA

#-------------------------------------------------------------

name = input("Qual é seu nome? ")
maiusculos = name.upper()
minusculos = name.lower()
namenospace = name.replace(" ","")
qletras = namenospace.__len__()
primeironame = name.split()
print("----------------------------------------------------------")
print(f"NOME EM MAIÚSCULO: {maiusculos}")  #name + .upper()
print(f"NOME EM MINÚSCULO: {minusculos}")  #name + .lowor()
print(f"NOME SEM ESPAÇO: {namenospace}")  #name + .replace(" ","")
print(f"QUANTAS LETRAS TEM: {qletras}")   #VAREAVEL DO .replace(" ","") + .__len__
print(f"PRIMEIRO NOME: {primeironame[0]}")  #name + .split() // colocar o numero [0] pois, é o primoro nome.

#--------------------------------------------------------------------

import random
numero_PC = random.randint(1, 100) #SORTEIO DE NUMEROS

#--------------------------------------------------------------------

number = int(input("Digite um numero: "))

if number % 2 == 0: # (% = MODULO) = é o resto da divisão
    print("O numero é PAR!")
else:
    print(f"numero é ÍMPAR!")