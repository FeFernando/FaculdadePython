alunos = [
    {"nome": "Ana", "notas": [8, 7, 9]},
    {"nome": "Carlos", "notas": [5, 6, 4]},
    {"nome": "Maria", "notas": [10, 9, 8]},
    {"nome": "João", "notas": [6, 7, 5]}
]


def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media



def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

for aluno in alunos:
    media = calcular_media(aluno["notas"])
    verifica = verificar_aprovacao(media)
    print(f"Nome: {aluno['nome']}, Nota: {media}, Status: {verifica}")