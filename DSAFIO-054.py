#                     CADASTRO DE TRABALHADOR EM PYTHON

from time import sleep
from datetime import datetime

cadastros = dict()

cadastros['Nome'] = str(input(' Nome: ')).strip().capitalize()
cadastros['Idade'] = int(input(' Ano do Nasimento: '))
cadastros['CTPS'] = int(input(' Carteira de Trabalho: '))
cadastros['Ano Contratação'] = int(input(' Ano de Contratção: '))
cadastros['Salário'] = float(input(' Salário: R$ '))

ano_atual = datetime.now().year
cadastros['Idade'] = ano_atual - cadastros['Idade']
cadastros['Aponsentarar com'] = cadastros['Idade'] + 35

print('=-=' * 30)
for k, v in cadastros.items():
    print(f' {k}: {v}')
    sleep(1)

