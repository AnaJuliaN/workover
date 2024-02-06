produtos = []
while True:
    nome =  input("Nome: ")
    produtos.append(nome)
    resp = input("Deseja continuar [S|N]? ")
    if resp.upper() == "N":
        break

# a função enumerate retorna simultaneamente o indice e elemento da lista

for indice, valor in enumerate(produtos):
    print("{} --> {}".format(indice, valor))