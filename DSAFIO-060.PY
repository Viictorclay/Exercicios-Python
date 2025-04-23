#                    SOMA DE NÚMEROS PARES COM FUNÇÃO


from random import randint
from time import sleep
lst = []


def sorteio():

    print(f'Sorteando numeros: ',end='')
    for f in range(1,6):
        
        numeros = randint(0,10)
        lst.append(numeros)
        print(f'{numeros} ', end='', flush=True )
        sleep(1)
    print('PRONTO!!')

def soma_de_par():

    soma = 0
    for n in lst:
        if n % 2 == 0:
            soma += n

    print(f'Somando os valores pares de {lst}, temos: {soma}')
    


sorteio()
soma_de_par()