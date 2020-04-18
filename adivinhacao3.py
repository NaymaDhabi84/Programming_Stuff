# coding=utf-8

import random

def jogar():

    print("*********************************")
    print("Bem-vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

                                  #total de tentativas + 1 ou o 4 mas fica uma má prática
    for rodada in range(1, total_de_tentativas + 1): #não precisa de parenteses para usar o FOR
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Voce digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue
        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto



        if (acertou):  #não é necessário o uso dos parenteses mas é uma boa prática
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
             print("Você errou! O seu chute foi maior do que o número secreto.")
             if(rodada == total_de_tentativas):
                print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            elif(menor):
             print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    #não há necessidade de incrementar, foi retirada a incrementação, o "for" já faz
    #podemos mudar os parâmetros tentativa {1} {0}. format( 1, 3)
    # e se for o formato R$2.59 então "R$ {:.2f}".format(1.59) .2 até 2 casas depos da ,

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
