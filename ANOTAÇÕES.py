
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