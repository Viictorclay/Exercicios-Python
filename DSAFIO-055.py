#                 CADASTRO DE UM JOGADOR DE FUTEBOL


gaveta = dict()
gaveta['Nome'] = str(input(' Qual é o nome do jogador ? ')).strip().capitalize()
gaveta['jogos'] = int(input(' Quantos jogos ele jogou ? '))
gaveta['gols'] = []
print('=-=' *30)

for c in range(gaveta['jogos']):
    gols = int(input(f' Quantos gols na {c+1}ª partida? '))
    gaveta['gols'].append(gols)

gaveta['Total'] = sum(gaveta['gols'])

print('=-=' * 30)
print('RESUMO: ')
print(f' Jogador: {gaveta["Nome"]}')
print(f' Partidas Jogadas: {gaveta["jogos"]}')
print(f' Total de Gols: {gaveta["Total"]}')
print('\nDesempenho por jogo:')
for i, g in enumerate(gaveta['gols']):
    print(f' ➤  Jogo {i+1}: {g} Gol(s)')