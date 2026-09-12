
usuarios = [
    {
        "nome": "Felipe",
        "idade": 30,
        "Profissão": "Programador"
    },
    {
        "nome": "Henrique",
        "idade": 46,
        "Profissão": "Biologo"
    }
]

nome = input("Digite o nome do usuario que deseja informação")
for usuario in usuarios:
    if usuario["nome"].lower() == nome.lower():
        print(f"Nome:{usuario["nome"]} - Idade: {usuario["idade"]}")
        break