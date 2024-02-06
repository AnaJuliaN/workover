'''Construa um programa que recaba a altura e sexo de uma pessoa. Baseado nas
fórmulas abaixo, calcule e mostre o peso ideal para essa pessoa:
    - No caso de homens: (72.7 * altura) - 58.0
    - No caso de mulheres: (62.1 * altura) - 44.7'''

sexo = input("Digite seu sexo [M | F]: ")
altura = float(input("Digite sua altura: "))

#nome.lower() - coloca tudo em minusculo
#nome.upper() - deixa em caixa alta

if sexo.upper() == "F":
    peso = (62.1 * altura) - 44.7
    print("Seu peso ideal é {:.2f}kg".format(peso))
elif sexo.upper() == "M":
    peso = (72.7 * altura) - 58.0
    print("Seu peso ideal é {:.2f}kg".format(peso))
else:
    print("Opção de sexo inválida.")
