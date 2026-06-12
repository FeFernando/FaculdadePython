

preco = float(input("Digite o preço do produto: "))

def calcular_imposto(preco):
    if preco < 11:
        imposto = preco * 0.1
    else:
        imposto = preco * 0.5
    return imposto

print(f"O imposto sobre seu produto foi de {calcular_imposto(preco):.2f}, preço final {preco+calcular_imposto(preco)}" )