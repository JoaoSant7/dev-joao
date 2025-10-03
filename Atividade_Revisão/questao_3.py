# Programa para calcular o fatorial de um número

# Solicita o número ao usuário
n = int(input("Digite um número inteiro positivo: "))

# Verificação de entrada
if n < 0:
    print("Não é permitido número negativo!")
else:
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    print(f"{n}! = {fatorial}")
