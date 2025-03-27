#                      SORTEIO DE NOMES


import random # SORTEIO

names = input(f"Quais são os alunos ? \n").split(",") # ESCOLHE ENTRE
names = [name.strip() for name in names] # REMOVE O ESPAÇO 
escolhido = random.choice(names)
print(" ")
print(f"O aluno(a) escolhido foi: {escolhido}")