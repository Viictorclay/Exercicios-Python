#                      FUNÇÃO ÁREA DE UM TERRENO


def linha():
    print('=-=' * 15)

def titulo():
    print()
    frase = 'Controle de Terrenos'
    print(f'{frase:>30}')
    linha()

def area(largura, comprimento):
    R = largura * comprimento
    print(f' A área de um terreo {largura}x{comprimento} é : {R}m²')
    linha()


while True:

    titulo()
    largura = float(input(' Largura (m): '))
    comprimento = float(input( ' Comprimento (m): '))
    area(largura, comprimento)
    continuar = str(input(' Deseja continuar (S/N) ? ')).upper().strip()
    if continuar in ['NÃO', 'NAO', 'N']:
        linha()
        print('Finalzado.. Até a próxima.')
        break
    if continuar in ['SIM', 'S']:
        linha()

