num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

# Garante que o loop percorra do menor para o maior número
if num1 > num2:
    num1, num2 = num2, num1

numeros_pares = []
for numero in range(num1, num2 + 1): #o 1 serve para incluir o número final
    # O operador de módulo % 2 == 0 verifica se o número é par
    if numero % 2 == 0:
        numeros_pares.append(numero)

print(f"Os números pares no intervalo entre {num1} e {num2} são: {numeros_pares}")