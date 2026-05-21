# Criar uma tabuada
for multiplicando in range(1, 6):  # Laço externo
    print(f"\n--- Tabuada do {multiplicando} ---")
    for multiplicador in range(1, 11):  # Laço interno (aninhado)
        resultado = multiplicando * multiplicador
        print(f"{multiplicando} × {multiplicador} = {resultado}")