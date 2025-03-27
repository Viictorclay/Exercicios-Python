#                    TRANSFORMAÇÃO DE TEXTO


name = input("Qual é seu nome? ")
maiusculos = name.upper()
minusculos = name.lower()
namenospace = name.replace(" ","")
qletras = namenospace.__len__()
primeironame = name.split()
print("-------------------------------------------------------")
print(f"NOME EM MAIÚSCULO: {maiusculos}")  #name + .upper()
print(f"NOME EM MINÚSCULO: {minusculos}")  #name + .lowor()
print(f"NOME SEM ESPAÇO: {namenospace}")  #name + .replace(" ","")
print(f"QUANTAS LETRAS TEM: {qletras}")   #VAREAVEL DO .replace(" ","") + .__len__
print(f"PRIMEIRO NOME: {primeironame[0]}")  #name + .split() // colocar o numero [0] pois, é o primoro nome.