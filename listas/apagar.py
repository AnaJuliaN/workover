alunos = ["Leticia"]            #0
alunos.append("Henrique")       #1
alunos.append("Leticia")        #2
alunos.append("Heitor")         #3
alunos.insert(4, "Ana Clara")   #4

alunos.pop(1) #se não colocar nenhum argumento ele remove sempre o ultimo elemento da lista
print(alunos)

#alunos.clear() -> remove todos os elementos da lista

#alunos.remove("Heitor") -> remove um elemento especificado da lista, mas remove somente a primeira ocorrencia
#por exemplo, no caso da leticia ira apagar somente a do primeiro indice, pois é a primeira ocorrencia
#caso queira remover mais de uma leticia fazemos um for com if, exemplo:
#for nome in alunos:
#    if nome == "Leticia":
#        alunos.remove(nome)
#print(alunos)
