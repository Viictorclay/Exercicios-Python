#                      leia apenas Int - FUNÇÃO


def leiaint(msg):

    while True:

        numero = input(msg)
        if numero.isnumeric():
            return int(numero)
        else:
            print(' ERRO! Digite um número interio.')


numero = leiaint(' Digite um número: ')
print(f' Você acabou de digitar o número: {numero}')