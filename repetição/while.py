print("COVID-19")

suspeitos = 0
num_pac = int(input("Informe a quantidade de pacientes: "))
cont = 0
while cont < num_pac:
    tosse = int(input("Tosse? \n1. Sim \n2. Não \nResp.: "))
    febre = int(input("Febre? \n1. Sim \n2. Não \nResp.: "))
    resp = int(input("Dificuldade de respirar? \n1. Sim \n2. Não \nResp.: "))

    if tosse == 1 and febre == 1 and resp == 1:
        suspeitos += 1

    cont += 1

print("Número de pessoas atendidas: {}".format(num_pac))
print("Suspeitos de COVID-19: {}".format (suspeitos))