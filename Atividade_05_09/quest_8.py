variaveis = ['a', 'b', 'c', 'd', 'e', 'f']
numeros = {}

for var in variaveis:
    while True:
        try:
            valor = float(input(f"Digite o número para a variável '{var}': "))
            numeros[var] = valor
            break  
        except ValueError:
            print("Erro: Por favor, digite apenas números. Tente novamente.")

produto = numeros['a'] * numeros['b'] * numeros['c'] * numeros['d'] * numeros['e'] * numeros['f']
print(f"O produto dos números selecionados é igual a {produto} ")

soma = numeros['a'] + numeros['b'] + numeros['c'] + numeros['d'] + numeros['e'] + numeros['f']

media = soma/6
print(f"A média dos números selecionados é igual a {media} ")