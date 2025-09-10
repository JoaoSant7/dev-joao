contador = 1
menor_numero = None # Inicializa a variável para o menor número

while contador <= 7:
    try:
        numero = int(input(f"Digite o {contador}º número inteiro: "))
        
        # Se é a primeira interação, o primeiro número é o menor
        if menor_numero is None or numero < menor_numero: #Assim, se o novo número for menor que o número anterior, ele se torna o menor número
            menor_numero = numero
            
        contador += 1
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

print(f"O menor número digitado foi: {menor_numero}")