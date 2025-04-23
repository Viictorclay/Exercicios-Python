#                  FUNÇÃO PARA QUALIFICAÇÃO DE VOTO


from datetime import datetime

def voto():
    
    print('-'* 30)
    ano = int(input(' Ano de nascimento: '))
    idade = datetime.now().year - ano
    if idade < 16:
        return print(f' Com {idade} anos: Não Vota.\n')
    elif idade <= 17:
        return print(f' Com {idade} anos: VOTO OPCIONAL.\n')
    elif idade >= 18:
        return print(f' Com {idade} anos: VOTO OBRIGATÓRIO.\n')
    elif idade >= 65:
        return print(f' Com {idade} anos: VOTO OPCIONAL.\n')

voto()