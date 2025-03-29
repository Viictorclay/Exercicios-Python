import random

lista = ["Pedra", "Papel", "Tisora"]

while True:
    
    escolha_do_pc = random.choice(lista).lower()

    
    m_escolha = input("Pedra, Papel ou Tisora? ").strip().lower()

    
    if m_escolha not in ["pedra", "papel", "tisora"]:
        print("Escolha inválida! Tente novamente.")
        continue

    print(f"ESCOLHA DA MÁQUINA: {escolha_do_pc.capitalize()}")

    if m_escolha == escolha_do_pc:
        print("EMPATE!")

    elif (m_escolha == "pedra" and escolha_do_pc == "tisora") or \
         (m_escolha == "papel" and escolha_do_pc == "pedra") or \
         (m_escolha == "tisora" and escolha_do_pc == "papel"):
        print("Você Venceu!")

    else:
        print("Você Perdeu!")

    comando = input("Deseja mais uma rodada? (sim/não) ").strip().lower()
    if comando in ["não", "nao"]:
        print("Certo, até a próxima.")
        break