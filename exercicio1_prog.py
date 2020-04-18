# coding=utf-8

#escreva uma função que receba três parâmetros (a,b e c) inteiros e retorne o maior valor entre os argumentos passados

print("***********************")
print("*** Qual é o maior? ***")
print("***********************")

print("Escolha três números (a,b e c) do grupo abaixo:")
print('[1,2,3,4,5,6,7,8,9,10]')


numero_a = int(input("Escolha o número a: "))
while numero_a < 1 or numero_a > 10:
    numero_a = raw_input("Número digitado não está dentro dos limites.\nEscolha o número a: ")

numero_b = int(input("Escolha o número b: "))
while numero_b < 1 or numero_b > 10:
    numero_b = raw_input("Número digitado não está dentro dos limites.\nEscolha o número b: ")

numero_c = int(input("Escolha o número c: "))
while numero_c < 1 or numero_c > 10:
    numero_c = raw_input("Número digitado não está dentro dos limites.\nEscolha o número c: ")


maior_numero = numero_a

if(numero_b > maior_numero):
     maior_numero = numero_b
if(numero_c > maior_numero):
    maior_numero = numero_c

print('O maior número entre a, b e c é: ', maior_numero)

print("Fim")
