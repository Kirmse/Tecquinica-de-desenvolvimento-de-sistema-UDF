#For
print("Números pares de 1 a 100:")

for numero in range(1, 101):
    if numero % 2 == 0:
        print(numero)

print('__' * 20)

#While

print("Números pares de 1 a 100:")
numero = 1
while numero <= 100:
    if numero % 2 == 0:
        print(numero)
    numero += 1
