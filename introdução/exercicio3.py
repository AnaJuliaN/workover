'''Escreva um programa que leia 3 números inteiros, calcule a escreva a média
aritmética entre eles'''

n1 = float(input("Digite o 1º número: "))
n2 = float(input("Digite o 2º número: "))
n3 = float(input("Digite o 3º número: "))

media = (n1 + n2 + n3)/3

print("Média aritmética = {:.2f}".format(media))