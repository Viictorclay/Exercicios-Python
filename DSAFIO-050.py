#               MENOR E MAIOR VALOR DE UMA LISTA


maior = menor = 0
valores = []
for c in range(0, 5):
    valores.append(int(input(f" Digite um valor {c}: ")))
print(f"{"=-=" * 30}")

print(f"Você digtou os valores {valores} ")
for c, v in enumerate(valores):

    if c == 0:
        maior = v
        menor = v
    else:
        if v > maior:
            maior = v
        elif v < menor:
            menor = v

print(f" O maior valor digitado foi {maior} nas posições ", end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f"{i}.. ", end='')

print(f"\n O menor valor digitado foi {menor} nas posições ", end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f"{i}.. ", end='')