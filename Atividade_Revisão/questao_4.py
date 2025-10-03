# Programa: Média da Turma com validação das notas

# Pergunta quantos alunos existem
qtd_alunos = int(input("Quantos alunos existem na turma? "))

soma_notas = 0

# Loop para cada aluno
for i in range(1, qtd_alunos + 1):
    nota = -1  # valor inicial inválido para entrar no while
    while nota < 0 or nota > 10:
        nota = float(input(f"Digite a nota do aluno {i} (0 a 10): "))
        if nota < 0 or nota > 10:
            print("❌ Nota inválida! Digite novamente.")
    soma_notas += nota

# Cálculo da média
media = soma_notas / qtd_alunos
print(f"\nA média da turma é: {media:.2f}")
