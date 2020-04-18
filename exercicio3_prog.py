# coding=utf-8

print("**********************************")
print("*** SOMA DA SEQUENCIA NUMÉRICA ***")
print("**********************************")

num1 = int(input("Digite o 1º valor: "))
num2 = int(input("Digite o 2 valor: "))
soma = 0

for i in range(num1, num2 + 1):
  soma += i

print("A soma da sequência numérica entre eles é {}: ".format(soma))

print("*** FIM ***")



