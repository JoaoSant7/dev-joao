try:
    numero_tabuada = int(input("Qual tabuada você deseja? (digite um número inteiro): "))
    inicio = int(input("Onde a tabuada deve começar? (digite um número inteiro): "))
    fim = int(input("Onde a tabuada deve terminar? (digite um número inteiro): "))
    print("-" * 20) #cria um separador com 20 hífens

    # Garante que o loop sempre vá do menor para o maior número
    if inicio > fim:
        inicio, fim = fim, inicio

    # Loop para gerar a tabuada
    for i in range(inicio, fim + 1):
        resultado = numero_tabuada * i
        print(f"{numero_tabuada} x {i} = {resultado}")

except ValueError:
    print("Entrada inválida. Por favor, digite apenas números inteiros.")