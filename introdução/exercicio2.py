'''Construa um programa que lei auma temperatura em Fahrenheint e converta-a
para Celsius. Sabe-se que: ºC = (ºF-32)/1.8'''

F = float(input("Digite a temperatura em Fahrenheint: "))

C = (F-32)/1.8

print("Celsius: {}".format(C))