import random

print ("=" * 40)

print("GERADOR DE NÚMEROS DA SORTE")

print("=" * 40)

nome = input("Qual é seu nome? ")
mes = int(input("Em que mes voce nasceu? (1-30)"))
dia = int(input("Em que dia você nasceu? (1-31)"))
#Gera 6 numeros entre 1 e 60
numeros_sorte = sorted(random.sample(range(1, 61), 6))
numero_especial = (mes + dia) % 10
print(f"Olá, {nome}!")
print(f"Seus numeros da sorte são: {numeros_sorte}")
print(f"Seu numero especial é: {numero_especial}")