#              UNIONDO DICIONARIO E LISTA



pasta = list()
pessoa = 0
soma_idade = 0

print('=-=' *30)
while True:
    gaveta = {}
    gaveta['nome'] = str(input(' \n Nome: ')).strip()
    gaveta['sexo'] = str(input(' Sexo (M/F): ')).strip().upper()
    gaveta['idade'] = int(input(' Idade: '))

    pasta.append(gaveta.copy())
    pessoa += 1
    soma_idade += gaveta['idade']

    continuar = input(' \nDeseja continuar ? (S/N) ').lower()
    if continuar in ['n','não','nao']:
        break

media_idd = soma_idade / pessoa

print('-=' * 30)
print(f'Cadastros: {pessoa}')
print(f'Media de idade: {media_idd} anos.')

print('\n Pessoas cadastradas:')
for p in pasta:
    print(f' - {p["nome"]}')

print('\nMulheres cadastradas:')
for p in pasta:
    if p['sexo'] == 'F':
        print(f' - {p["nome"]}')

