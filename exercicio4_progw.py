# coding=utf-8

print("*****************************")
print("**** Fatorial com WHILE *****")
print("*****************************")

n = int(input("Digite um número e descubre seu fatorial: "))
contador = n
f = 1

print("Calculando {}! ".format(n), "\n")

while contador > 0:
 print("{} ".format(contador), "\n")
 print("x" if contador > 1 else " = ")
 f = f * contador
 contador -= 1

print("{}! é: {} ".format(n, f))
print("*** FIM ***")


