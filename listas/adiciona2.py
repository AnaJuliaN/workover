frutas = []
while True:
    nome = input("Digite o nome de uma fruta: ")
    frutas.append(nome)

    resp = input("Deseja continuar [S|N]? ")
    if resp.upper() == "N":
        break
for nome in frutas:
    print(nome)