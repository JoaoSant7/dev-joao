numero = int(input("Digite um número inteiro positivo: "))

for i in range(numero, 0, -1):  # começa do número até 1
    if i % 2 != 0:  # verifica se é ímpar
        print(i)
