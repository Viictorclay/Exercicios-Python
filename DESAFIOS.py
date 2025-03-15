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

n = int(input("Digite um numero: "))
suce = n + 1
ante = n - 1
print(f"O Sucessor do numero {n} é {suce}")
print(f"O Antecessor do numero {n} é {ante}")
print(f" {ante} , {n} , {suce} ")

#------------------------------3------------------------------
#       O DOBRO, TRIPLO E A RAIZ QUADRADA DE UM NUMERO

n = int(input("Digite um numero: "))
d = n * 2
t = n * 3
rq = n ** (1/2)
print(f"O dobro de {n} é {d}.")
print(f"O triplo de {n} é {t}.") 
print(f"A raiz quadrada de {n} é {rq}.")
print(f"NUMERO: {n}")
print(f"DOBRO: {d}")
print(f"TRIPLO: {t}")
print(f"RAIZ QUADRADA: {rq}")

#------------------------------3------------------------------
#                 CALCULAR A MEDIA DE UM ALUNO

print("-----------------------------------------------------")
print("                   NOTA DE CLAY                      ")
print("-----------------------------------------------------")
pn = float(input(" Primeira nota: "))
sn = float(input(" Segunda nota: "))
md = (pn + sn) / 2
print("-----------------------------------------------------")
print(f" MEDIA: {md}")
if md >= 6:
    print(" ALUNO APROVADO! ")
else:
    print(" ALUNO EM RECUPERÇÃO! ")
       
#------------------------------4------------------------------
#     CONVERSOR DE METROS PARA CENTIMETROS E MILIMETROS

m = float(input("Quantos metros ? "))
cm = m * 100
mm = m * 1000
print("-----------------------------------------------------")
print(f"Metros: {m}m")
print(f"Em centimetros: {cm}cm")
print(f"Em milimetros: {mm}mm")

#------------------------------5------------------------------
#                 TABUADA DE UM NUMERO INTERIO

n = int(input("Digite um numero: "))
a = n * 1
b = n * 2
c = n * 3
d = n * 4
e = n * 5 
f = n * 6
g = n * 7
h = n * 8
i = n * 9
j = n * 10
print(f"{n} x 1 = {a}")
print(f"{n} x 2 = {b}")
print(f"{n} x 3 = {c}")
print(f"{n} x 4 = {d}")
print(f"{n} x 6 = {f}")
print(f"{n} x 7 = {g}")
print(f"{n} x 8 = {h}")
print(f"{n} x 9 = {i}")
print(f"{n} x 10 = {j}")

#------------------------------6------------------------------
#     QUANTOS DOLAS POSSO COMPRAR COM DINEHRO QUE TENHO ?

dinheiro = float(input("Quanto você tem ? "))
dola = dinheiro / 5.74
print(f"Vocês compará ${dola:.2f} dolares.")

#------------------------------7------------------------------
#                   PROGRAMA PARA PINTORES

altura = float(input("Qual é altura em M: "))
largura = float(input("Qual é a largura em M: "))
area = altura * largura
litros = area / (area ** 2)
print(f"Você ira gastar {litros:.3f} litros por m2.")

