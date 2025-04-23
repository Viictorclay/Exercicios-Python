#               ficha de um jogador - FUNÇÃO


def ficha(nome='<desconhecido>', gols=0):

    print(f' O jogador {nome} fez {gols} gol(s) no Campeonato.\n{"-"*55}\n')

print(f'\n{'-'*55}')
nome = str(input(' Nome do jogador: ')).capitalize()
gols = str(input(' Número de Gols: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    nome = 'DESCONHECIDO'


ficha(nome, gols)