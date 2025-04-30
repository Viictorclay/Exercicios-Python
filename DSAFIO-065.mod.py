from modulosV import moeda


p = float(input('\n Digite o preço: R$'))
print(f' A Metade do {p} é --> R${moeda.metade(p)}')
print(f' O dobro de {p} é --> R${moeda.dobro(p)}')
print(f' Aumentando 10%, temos --> R${moeda.aumento(p)}')
print(f' Disconto de 13%, temos --> R${moeda.disconto(p)}\n')