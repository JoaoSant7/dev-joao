# Programa: Verificador de Turma

alguem_reprovou = False  # flag inicial

print("Digite as notas de 5 alunos (0 a 10):")

for i in range(1, 6):
    # Validação da nota
    while True:
        nota = float(input(f"Nota do aluno {i}: "))
        if 0 <= nota <= 10:
            break
        print("❌ Nota inválida! Digite um valor entre 0 e 10.")

    # Verifica se o aluno reprovou
    if nota < 5.0:
        alguem_reprovou = True

# Resultado final
if alguem_reprovou:
    print("\nA turma possui pelo menos um aluno reprovado.")
else:
    print("\nParabéns! Todos na turma foram aprovados.")
