#                                  MSG COM BORDAS NA MEDIDA


def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


msg = str(input(' Escreva uma frase: '))
escreva(msg)