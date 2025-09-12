try:
    numero = int(input("Digite um número inteiro para verificar se ele é perfeito: "))

    # Números perfeitos são positivos, então lidamos com entradas inválidas
    if numero <= 0:
        print("A definição de número perfeito se aplica apenas a números positivos.")
    else:
        soma_divisores = 0

        # Encontra os divisores e os soma
        for i in range(1, numero):
            if numero % i == 0:
                soma_divisores += i

        # Verifica se a soma dos divisores é igual ao número
        if soma_divisores == numero:
            print(f"O número {numero} é um número perfeito.")
        else:
            print(f"O número {numero} não é um número perfeito.")

except ValueError:
    print("Entrada inválida. Por favor, digite apenas números inteiros.")
