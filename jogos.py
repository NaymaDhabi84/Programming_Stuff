# coding=utf-8

import forca
import adivinhacao3

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha seu jogo**********")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo?: "))

    if(jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif(jogo == 2):
        print("jogando Adivinhação")
        adivinhacao3.jogar()

print("Fim do jogo")

if(__name__  == "__main__"):
    escolhe_jogo()
