#DIAGONAL PRIMÁRIA (DP)
#    i = j

#DIAGONAL SECUNDÁRIA (DS)
#    i + j = ORDEM + 1

'''Construa um programa no qual o usuário informe a ordem de uma matriz quadrada.
Em seguida, o programa deve gerar valores aleatórios para essa matriz no intervalo
[1, 10].

Ao fim, o programa deve calcular e imprimir a média aritmética entre o maior elemento
da diagonal principal e o menor elemento da diagonal secundária.'''

import random

ordem = int(input("Digite a ordem da matriz: "))
if ordem >= 2:
    while True:
        M = []
        for i in range(ordem):
            LINHA = []
            for j in range(ordem):
                num = random.randint(1, 10)
                LINHA.append(num)
            M.append(LINHA)
        break
    
    DP = []
    DS = []
    for i in range(ordem):
        for j in range(ordem):
            print(M[i][j], end = " ")
            if i == j: #DP
                DP.append(M[i][j])
            elif i + j == (ordem - 1): #DS
                DS.append(M[i][j])
        print("")
    maior_DP = max(DP)
    menor_DS = min(DS)
    media = (maior_DP + menor_DS) / 2
    print("Média = {}".format(media))
else:
    print("Informe uma ordem válida.")