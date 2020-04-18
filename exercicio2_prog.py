# coding=utf-8

print("*******************************")
print("*** Números pares e ímpares ***")
print("*******************************")

lista_completa = [1,2,3,4,5,6,7,8,9,10]
lista_pares = []
lista_impares = []


for numero in lista_completa:
    if numero % 2 == 0:
        lista_pares.append(numero)

print(lista_pares)

for numero in lista_completa:
    if numero % 2 != 0:
        lista_impares.append(numero)

print(lista_impares)


