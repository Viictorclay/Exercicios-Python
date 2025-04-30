from modulosV import moeda


p = float(input('\n Digite o preço: R$'))
print(f' A Metade do {moeda.formatado(p)} é --> {moeda.formatado(moeda.metade(p))}')
print(f' O dobro de {moeda.formatado(p)} é --> {moeda.formatado(moeda.dobro(p))}')
print(f' Aumentando 10%, temos --> {moeda.formatado(moeda.aumento(p))}')
print(f' Disconto de 13%, temos --> {moeda.formatado(moeda.disconto(p))}\n')