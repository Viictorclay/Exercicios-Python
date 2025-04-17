#                        menor e maior numero com FUNÇÃO



def lin():
    print('=-=' * 15)

def inicio(valores):

    for i, v in enumerate(valores):

        if i == 0:
            maior = v
            menor = v
        else:
            if v > maior:
                maior = v
            elif v < menor:
                menor = v

    lin()
    print(f' Você digitou os núemros: {valores} ')
    lin()
    print(f' O maior número é {maior}')
    print(f' O menor número é {menor}')

# não dá para fazer direto, tenho que fazer a entrada número e depois coinverter ele para 'int'
entrada = input(' digete 1 ou mais números: ')
valores = [int(n) for n in entrada.split()]
inicio(valores)