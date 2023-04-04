# Game Pedra, Papel, Tesoura
import random

# Opções do jogo
opcoes = ["pedra", "papel", "tesoura"]

# Função para jogar
def jogar():
    # Pergunta ao usuário qual opção ele escolhe
    jogador = input("Escolha pedra, papel ou tesoura: ").lower()
    
    # Seleciona uma opção aleatória para o computador
    computador = random.choice(opcoes)
    
    # Verifica quem ganhou
    if jogador == computador:
        print("Empate!")
    elif jogador == "pedra":
        if computador == "papel":
            print("Você perdeu! O computador escolheu papel.")
        else:
            print("Você ganhou! O computador escolheu tesoura.")
    elif jogador == "papel":
        if computador == "tesoura":
            print("Você perdeu! O computador escolheu tesoura.")
        else:
            print("Você ganhou! O computador escolheu pedra.")
    elif jogador == "tesoura":
        if computador == "pedra":
            print("Você perdeu! O computador escolheu pedra.")
        else:
            print("Você ganhou! O computador escolheu papel.")
    else:
        print("Opção inválida. Tente novamente.")
    
    # Pergunta se o usuário quer jogar novamente
    jogar_novamente = input("Quer jogar novamente? (sim/não)").lower()
    if jogar_novamente == "sim":
        jogar()
    else:
        print("Obrigado por jogar!")
        print("Volte sempre!")

# Inicia o jogo
jogar()
