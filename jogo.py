import random

def jogo():
    usuario= input("'r' para pedra, 's' para tesoura e 'p' para papel  ")
    computador= random.choice(['r','p','s'])

    if usuario == computador:
        return "É um empate!"

    if vencedor(usuario,computador):
        return "Você ganhou!"

    return "Você perdeu :("

def vencedor(jogador,oponente):
    if (jogador == 'r' and oponente == 's') or (jogador=='s' and oponente=='p') or (jogador=='p' and oponente=='r'):
        return True

print(jogo())