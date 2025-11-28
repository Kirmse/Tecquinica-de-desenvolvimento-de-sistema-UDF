alunos = []

quantidade = int(input("Quantos alunos deseja cadastrar? "))

for n in range(quantidade):
    nome = input(f"Digite o nome do aluno {n + 1}: ")
    alunos.append(nome)

print("\nAlunos cadastrados:")
for nome in alunos:
    print(f"Aluno: {nome}")