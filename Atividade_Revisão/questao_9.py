# Programa: Classificação por idade

# Contadores
criancas = 0
adolescentes = 0
adultos = 0
idosos = 0

print("Digite a idade de 10 pessoas:")

for i in range(1, 11):
    # Validação da idade
    while True:
        idade = int(input(f"Idade da pessoa {i}: "))
        if idade >= 0:
            break
        print("Idade inválida! Digite um número maior ou igual a 0.")

    # Classificação
    if 0 <= idade <= 12:
        criancas += 1
    elif 13 <= idade <= 17:
        adolescentes += 1
    elif 18 <= idade <= 59:
        adultos += 1
    else:
        idosos += 1

# Exibe resultado
print("\nClassificação por idade:")
print(f"Crianças (0-12 anos): {criancas}")
print(f"Adolescentes (13-17 anos): {adolescentes}")
print(f"Adultos (18-59 anos): {adultos}")
print(f"Idosos (60+ anos): {idosos}")
