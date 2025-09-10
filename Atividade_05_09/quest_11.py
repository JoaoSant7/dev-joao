num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

# Garante que o loop percorra do menor para o maior número
if num1 > num2:
    num1, num2 = num2, num1

soma_impares = 0
for numero in range(num1, num2 + 1):
    # O operador de módulo % 2 != 0 verifica se o número é ímpar. Se for == 0 o número é par.
    if numero % 2 != 0:
        soma_impares += numero

print(f"A soma de todos os números ímpares no intervalo é: {soma_impares}")