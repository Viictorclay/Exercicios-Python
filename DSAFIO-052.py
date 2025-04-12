#                    DICIONARIO EM PYTHON


dicionario = dict()

dicionario['Nome'] = str(input(' Nome do aluno: '))
dicionario['Media'] = float(input(' Media do aluno: ').replace(",","."))
print('=-=' * 30)
print(f' NOME DO ALUNO: {dicionario["Nome"]}')
print(f' MEDIA: {dicionario["Media"]}')
if dicionario['Media'] >= 6:
    print(' Situação do aluno: Aprovado')
else:
    print(' Situação do aluno: Em Recuperação')
print('=-=' * 30)