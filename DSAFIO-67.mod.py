from modulosV import moeda


p = float(input('\n Digite o preço: R$'))#.replace(".","").replace(".",",").strip()
print(f' A Metade do {moeda.formatado(p)} é --> {moeda.metade(p, True) }')
print(f' O dobro de {moeda.formatado(p)} é --> {moeda.dobro(p, True)}')
print(f' Aumentando 10%, temos --> {moeda.aumento(p, True)}')
print(f' Disconto de 13%, temos --> {moeda.disconto(p, True)}\n')