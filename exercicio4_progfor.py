# coding=utf-8

print("******************************")
print("**** Fatorial com FOR ********")
print("******************************")

num = int(input("Digite um número e descubra seu fatorial: "))

print("Calculando {}! ".format(num), "\n")

resultado = 1

for num in range(1, num + 1):
    resultado = resultado * num

print("{}! é: {} ".format(num, resultado))
print("*** FIM ***")




