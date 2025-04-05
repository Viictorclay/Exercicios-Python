
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

#--------------------------------------------------------------------
#                           CORES NO TERMINAL

#                \033[0;33;44m
#________________________________________________
#     STYLER     |     TEXT      |      BACK     |
# 0 = None       | 30 = WHITE    | 40 = WHITE    |
# 1 = Bold       | 31 = RED      | 41 = RED      |
# 4 = Underline  | 32 = GREEN    | 42 = GREEN    |
# 7 = negative   | 33 = YELLOW   | 43 = YELLOW   |
#                | 34 = BLUE     | 44 = BLUE     |
#                | 35 = PURPLE   | 45 = PURPLE   |
#                | 36 = CYAN     | 46 = CYAN     |
#                | 37 = GRAY     | 47 = GRAY     |
#________________|_______________|_______________|

# 30      black         preto         40
# 31      red           vermelho      41
# 32      green         verde         42
# 33      yellow        amarelo       43
# 34      blue          azul          44
# 35      Magenta       Magenta       45
# 36      cyan          ciano         46
# 37      grey          cinza         47
# 97      white         branco       107

#------------------------------------------------------------------------

menor = 0
maior = 0
for c in range(1, 4):
    peso = float(input(f"Peso da pessoa {c} : "))
    if c == 1:
        maior = peso #O PRIMEIRO PESO SENDO MAIOR OU MENOR RECEBE
        menor = peso #O PRIMEIRO PESO SENDO MAIOR OU MENOR RECEBE
    else:
        if peso > maior: #AGORA, SE O PROXIMO PESO FOR MAIOR
            maior = peso #OS NUMEROS SÃO TROCADOS E O NOVO NUEMRO É POSTO O LUGAR.
        if peso < menor: #SE O PROXIMO NUMERO FOR MENOR QUE FOI DIGITADO
            menor = peso #A VAREAVEL RECEBE O NOVO MEOR NUMERO  
print(f"MAIOR PESO: {maior}Kg")
print(f"MENOR PESO: {menor}Kg")

#-----------------------------------------------------------------------------------------

max() # maior numero dentre as vareáveis
min() # menor numero dentre as vareáveis
exit() # finaliza o programa \ caso esteja dentro de um loop, não precisa usar o BREACK

#----------------------------------------------------------------------------------------------

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("                 BANCO Cy                  ")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
valor = int(input(" Que valor você quer sacar ? R$ "))
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

notas_50 = notas_20 = notas_10 = notas_1 = 0

notas_50 = valor // 50 # divisão inteira/ quantas notas de 50 cabe dentro do numero (valor)
valor %= 50 # o resto do valor

notas_20 = valor // 20 # divisão inteira/ quantas notas de 20 cabe dentro do numero (valor)
valor %= 20 # resto da divisão

notas_10 = valor // 10# divisão inteira/ quantas notas de 10 cabe dentro do numero (valor)

valor %= 10 # resto da divisão

notas_1 = valor // 1 # divisão inteira/ quantos notas de 1 cabe dentro do valor
valor %= 1 # resto da divisão


#!!!!!! A SOBRA É PASSADA ATÉ NÃO TER COMO FAZER AS DIVISÕES INTEIRAS OU CHEGAR NO 1 !!!!!!!

#-------------------------------------------------------------------------------------------------

total = 0 # 0 só para nascer a vareavel
produtoM1000 = 0
menor_preço = None # "NONE" Significa que ira receber um valor que ainda não sei
nomeD_menor = "" # "" Denominando que vai vim uma String

print("=-=-=-=-=--=--=--=-=---=-=-=-=-=-=-=-=-=-=-=-=")

while True:

    nomeD_produto = input("Produto: ")
    preço = float(input("Preço: R$"))
    
    total += + preço # colocar ou não o "+" não muda nesse caso

    if preço > 1000:
        produtoM1000 += +1 # colocar ou não o "+" não muda nesse caso

    escolha = input("Tem mais algum produto ? (sim/não) ").strip().lower()

    if menor_preço is None or preço < menor_preço: # Se menor_preço é NONE or preço < menor_preço
        menor_preço = preço # menor_preço vai receber (novo) preço
        nomeD_menor = nomeD_produto # nomeD_menor vai receber o nomeD_produto

        # Ou seja, quando encontrar um produto com preço menor, acontece:
        
        # - O novo preço é colocado em "menor_preço"
        # - O nome do produto é salvo em "nomeD_menor"
