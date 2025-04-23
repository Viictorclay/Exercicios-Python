#                         FUNÇÃO PARA VOTAÇÃO


from datetime import datetime

def voto():
    
    ano = int(input(' Ano de nascimento: '))
    idade = datetime.now().year - ano
    if idade < 16:
        return print(' Sua votação é NEGADA.')
    elif idade <= 17:
        return print(' Sua votação é OPCIONAL.')
    elif idade >= 18:
        return print(' Sua votação é OBRIGATORIA.')

voto()