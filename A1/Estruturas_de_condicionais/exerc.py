idade = int(input("Digite a sua idade: "))

if idade < 0:
    print("Idade inválida.")
elif idade < 14:
    print("Entrada proibida para menores de 14 anos.")
elif idade < 18:    
    print("Entrada permitida somente com acompanhante maior de 18 anos.")
else:
    print("Entrada liberada. Aproveite o evento!")