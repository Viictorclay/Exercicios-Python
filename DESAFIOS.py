#------------------------------1------------------------------
#                     CALCULAR UM NUMERO

#n1 = int(input("Digite um numero: "))
#n2 = int(input("Digite outro numero: "))
#s = n1 + n2
#print("A soma entre {} e {} vale {}".format(n1, n2, s))

#------------------------------2------------------------------
#                TIPO PRIMITIVO & SUAS INFORs

#print(type(n))
#print(f"Só tem espaços?{n.isspace()}") #.isspace   SÓ ESPAÇO
#print(f"È numerorico?{n.isnumeric()}") #.isnumeric NUMERO
#print(f"È alfabetico?{n.isalpha()}") #.isalpha     LETRAS
#print(f"È Alfanumerico?{n.isalnum()}") #.isalnum  NUMERO&LETRA
#print(f"Está em letras MAIÚSCULAS?{n.isupper()}") #.isupper
#print(f"Está em letras minúsculas?{n.islower()}") #.islower

#------------------------------3------------------------------
#             SUCESSOR E O ANTECESSOR DE UM NUMERO

#n = int(input("Digite um numero: "))
#suce = n + 1
#ante = n - 1
#print(f"O Sucessor do numero {n} é {suce}")
#print(f"O Antecessor do numero {n} é {ante}")
#print(f" {ante} , {n} , {suce} ")

#------------------------------3------------------------------
#       O DOBRO, TRIPLO E A RAIZ QUADRADA DE UM NUMERO

#n = int(input("Digite um numero: "))
#d = n * 2
#t = n * 3
#rq = n ** (1/2)
#print(f"O dobro de {n} é {d}.")
#print(f"O triplo de {n} é {t}.") 
#print(f"A raiz quadrada de {n} é {rq}.")
#print(f"NUMERO: {n}")
#print(f"DOBRO: {d}")
#print(f"TRIPLO: {t}")
#print(f"RAIZ QUADRADA: {rq}")

#------------------------------3------------------------------
#                 CALCULAR A MEDIA DE UM ALUNO

#print("-----------------------------------------------------")
#print("                   NOTA DE CLAY                      ")
#print("-----------------------------------------------------")
#pn = float(input(" Primeira nota: "))
#sn = float(input(" Segunda nota: "))
#md = (pn + sn) / 2
#print("-----------------------------------------------------")
#print(f" MEDIA: {md}")
#if md >= 6:
#    print(" ALUNO APROVADO! ")
#else:
#    print(" ALUNO EM RECUPERÇÃO! ")
       
#------------------------------4------------------------------
#     CONVERSOR DE METROS PARA CENTIMETROS E MILIMETROS

#m = float(input("Quantos metros ? "))
#cm = m * 100
#mm = m * 1000
#print("-----------------------------------------------------")
#print(f"Metros: {m}m")
#print(f"Em centimetros: {cm}cm")
#print(f"Em milimetros: {mm}mm")

#------------------------------5------------------------------
#                 TABUADA DE UM NUMERO INTERIO

#n = int(input("Digite um numero: "))
#a = n * 1
#b = n * 2
#c = n * 3
#d = n * 4
#e = n * 5 
#f = n * 6
#g = n * 7
#h = n * 8
#i = n * 9
#j = n * 10
#print(f"{n} x 1 = {a}")
#print(f"{n} x 2 = {b}")
#print(f"{n} x 3 = {c}")
#print(f"{n} x 4 = {d}")
#print(f"{n} x 6 = {f}")
#print(f"{n} x 7 = {g}")
#print(f"{n} x 8 = {h}")
#print(f"{n} x 9 = {i}")
#print(f"{n} x 10 = {j}")

#------------------------------6------------------------------
#     QUANTOS DOLAS POSSO COMPRAR COM DINEHRO QUE TENHO ?

#dinheiro = float(input("Quanto você tem ? "))
#dola = dinheiro / 5.74
#print(f"Vocês compará ${dola:.2f} dolares.")

#------------------------------7------------------------------
#                   PROGRAMA PARA PINTORES

#altura = float(input("Qual é altura em M: "))
#largura = float(input("Qual é a largura em M: "))
#area = altura * largura
#litros = area / 2
#print(f"Você ira gastar {litros:.3f} litros por m2.")

#------------------------------8------------------------------
#             LOJA AQUI TUDO TEM DE 5% DESCONTO !!

#print("-----------------------------------------------------")
#valor = float(input("Qual é o valor do produto? "))
#vdescontado = valor -  (valor * 5/100)
#sodesconto = vdescontado - valor
#print("-----------------------------------------------------")
#print(f"VALOR SEM DESCONTO: R$ {valor}")
#print(f"VALOR COM DESCONTO: R$ {vdescontado:.2f}")
#print(f"DESCONTO DE: R$ {sodesconto}")
#print("-----------------------------------------------------")

#------------------------------9------------------------------
#                      REAJUSTE SALARIAL

#salario = float(input("Quanto o fucionariol ganha? "))
#salarioCR = salario + (salario * 8.40/100)
#reajuste = salarioCR -  salario
#print(f"O salario do funcionario ficou R${salarioCR}")
#print(f"O reajuste foi de R${reajuste}")

#------------------------------10------------------------------
#                    CELSIUS PRA FAHRENHEIT

#c = float(input("Quantos graus está fazendo? "))
#f = (c * 9/5) + 32
#print(f"CELSIUS: {c}°C")
#print(f"FAHRENHEIT: {f}°F")

#------------------------------11------------------------------
#                      ALUGUEL DE CARRO

#dias = int(input("Quantos dias? "))
#kms = float(input("Quantos kms rodou? "))
#pagar = (dias * 60) + (kms * 0.15)
#print(f"Falor final: {pagar:.2f}")

#------------------------------12------------------------------
#


#import math
#num = float(input("Digite um numero: "))
#arredondarCIMA = math.ceil(num)
#arredondarBAIXO = math.floor(num)
#partINTERIA = math.trunc(num)
#potencia = math.pow(num)
#raizQ = math.sqrt(num)

#print(f"ARREDONDANDO PARA CIMA: {arredondarCIMA}")
#print(f"ARREDONDANDO PARA BAIXO: {arredondarBAIXO}")
#print(f"PARTE INTEIRA: {partINTERIA}")
#print(f"POTENCIA: {potencia}")
#print(f"RAIZ QUADRADA: {raizQ:.2f}")

#------------------------------13------------------------------
#

import random # SORTEIO

names = input(f"Quais são os alunos ? \n").split(",") # ESCOLHE ENTRE
names = [name.strip() for name in names] # REMOVE O ESPAÇO 
escolhido = random.choice(names)
print(" ")
print(f"O aluno(a) escolhido foi: {escolhido}")
