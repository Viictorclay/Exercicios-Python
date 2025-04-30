#                Calculadora de hábitos saudáveis


from datetime import datetime
import os

dados = dict()
data_atual = datetime.now()

historico = {}
data_str = data_atual.strftime("%d/%m/%Y")
historico[data_str] = dados

def cadastrar_dados_diarios():
    print(f'\n Eaii {dados["nome"]}, vamos ver se você está tendo abitos saudáveis! 😃')
    print('-'*65)
    dados['agua'] = int(input(" Quantos litros de água bebeu? "))
    dados['sono'] = int(input(' Quantas horas você dormiu? '))
    dados['atv_física'] = input(' Fez alguma atividade física? ')
    dados['alimentação'] = int(input(' Fez quantas refeições? '))
def avaliar_habitos():
    if  dados['agua'] < 2:
        print(' 💧 Pouca ingestão de água. Tente beber pelo menos 2L por dia.')
    else:
        print(' ✅ Boa ingestão de água!')
    if dados['sono'] <= 6:
        print(' 😴 Poucas horas de sono. Tente dormir ao menos 7-8h.')
    else:
        print(' ✅ Boa qualidade de sono!')
    if dados['atv_física'].lower() in ['não', 'nao', 'n']:
        print(' 🏃‍♂️  Sem atividade física. Mexer o corpo é importante!')
    else:
        print(' ✅ Boa, praticar atividade física é essencial.')
    if dados['alimentação'] < 3:
        print(' 🍽️  Poucas refeições. O ideal é de 4 a 6 por dia.')
    else:
        print(' ✅ Alimentação equilibrada.')

def exibir_feedback():
    print('\n RESUMO DO DIA:', dados['nome'])
    print(' Data de hoje:', data_atual.strftime("%d/%m/%Y"))
    print(' Hora:', data_atual.strftime("%H:%M"))
    print('-'*65)
    avaliar_habitos()

def clear_sytem():
    os.system('cls' if os. name == 'nt' else 'clear')


# programa principal

while True:

    dados['nome'] = input(' Nome: ')
    clear_sytem()
    cadastrar_dados_diarios()
    exibir_feedback()
    pergunta = input(' \n Deseja ver o hitorico 🤔 ? ')
    if pergunta.lower() in ['não', 'nao', 'n']:
        hst = input(' Mas deseja Continuar 🤔 ? ')
        if hst.lower() in ['não', 'nao', 'n']:
            print(' Ok. Até a proxima. 😊')
            break
        else:
            clear_sytem()
    else:
        print(historico)
        continuar = input(' \nDeseja continuar ? ')
        if continuar.lower() in ['não', 'nao', 'n']:
            vhist = input(' Mas deseja ver o Historico 🤔 ? ')
            if vhist.lower() in ['não', 'nao', 'n']:
                print(' Ok. Até a proxima. 😊')
                break
            else:
                print(historico)
                break
        else:
            print()