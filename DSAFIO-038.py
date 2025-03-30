#                QUANTAS JÁ ATIGIRAM A MAIOR IDADE?


ttmaior = 0
ttmenor = 0
for c in range(1, 7):
    ano = int(input("ANO DE NASCIMENTO: "))
    r = 2025 - ano
    if r >= 18:
        ttmaior += +1
    else:
        ttmenor += +1
print(f"{ttmaior} São maiores de idade.")
print(f"{ttmenor} São menores de idade.")