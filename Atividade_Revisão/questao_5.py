# Programa: Contar vogais e consoantes em uma frase

frase = input("Digite uma frase: ")

# Vogais
vogais = "aeiouAEIOU"
qtd_vogais = 0
qtd_consoantes = 0

for char in frase:
    if char.isalpha():  # considera apenas letras
        if char in vogais:
            qtd_vogais += 1
        else:
            qtd_consoantes += 1

print(f"\nResultado:")
print(f"Vogais: {qtd_vogais}")
print(f"Consoantes: {qtd_consoantes}")
