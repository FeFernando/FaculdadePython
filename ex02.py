soma = 0
while True:
    numero = int(input("Digite um numero: "))

    if numero == 0:
        break
    soma += numero
print("A soma de todos os numeros foi ", soma)