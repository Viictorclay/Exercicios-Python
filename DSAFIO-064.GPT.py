#                Calculadora de hábitos saudáveis

dados = dict()
def cadastrar_usuario():
    dados['nome'] = input(' Nome: ')
def cadastrar_dados_diarios():
    print('-'*55)
    dados['agua'] = int(input(" Quantos ML's de água bebeu? "))
    dados['sono'] = int(input(' Quantas horas você dormiu? '))
    dados['atv_física'] = input(' Fez alguma atividade física? ')
    dados['alimentação'] = int(input(' Fez quantas refeições? '))
    

def avaliar_habitos():
    if  dados['agua'] < 1000:
        print(' pouca água..')

def exibir_feedback():



cadastrar_usuario()
cadastrar_dados_diarios()
avaliar_habitos()
print(dados)