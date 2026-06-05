import random
num = random.randint(1, 100)
choice = int(input("Digite um numero de 1 a 100: \n"))
if num == choice:
    print("Você acertou!")
else:
    print(f"Que pena o numero era {num}")