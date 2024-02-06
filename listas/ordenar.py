#Criação de uma lista
praias_RN = []

#inclusão de elementos
#forma 1
praias_RN = ["Pipa"]
#forma 2
praias_RN.append("Maracajaú")
praias_RN.append("Genipabu")
praias_RN.append("pipa") #na ordenação as letras maiusculas são ordenas primeiro que as minusculas numa lista
#forma 3
praias_RN.insert(2, "Ponta Negra")

praias_RN.sort()
#praias_RN.sort(reverse = True) -> reverse ordena decrescentemente

for praia in praias_RN:
    print(praia)
