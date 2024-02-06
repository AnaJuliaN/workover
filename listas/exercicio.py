'''Crie um programa que solicite o usuário um número N ímpar, maior que 1. Em
seguida, preencha uma lista com N números positivos. Selecione o elemento que
está no centro da lista. Ao final, calcule e escreva o fatorial do elemento selecionado.'''

N = int(input("Digite um valor N impar maior que 1: "))
if N > 1 and N % 2 != 0:
    num_validos = 0
    valores = []
    while num_validos < N:
        num = int(input("Digite um número inteiro positivo: "))
        if num > 0:
            num_validos += 1
            valores.append(num)
    indice_centro = int(len(valores) / 2)
    print("Elemento que está no centro da lista: {}".format(valores[indice_centro]))
    fat = 1
    #4! = 4 * 3 * 2 * 1
    for n in range(1, valores[indice_centro] + 1):
        fat = fat * n
    print("Fatorial do valor encontrado no centro da lista: {}! = {}".format(valores[indice_centro], fat))
else:
    print("Você não informou um valor para N impar maior que 1.")