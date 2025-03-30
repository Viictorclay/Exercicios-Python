#                       MAIOR PESO E MENOR PESO.


menor = 0
maior = 0
for c in range(1, 4):
    peso = float(input(f"Peso da pessoa {c} : "))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso    
print(f"MAIOR PESO: {maior}Kg")
print(f"MENOR PESO: {menor}Kg")