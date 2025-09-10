contador = 1
positivos = 0
negativos = 0
zeros = 0

while contador <= 8:
    try:
        numero = int(input(f"Digite o {contador}º número inteiro: "))
        
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        else:
            zeros += 1
            
        contador += 1
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

print("\nResultados:")
print(f"Quantidade de números positivos: {positivos}")
print(f"Quantidade de números negativos: {negativos}")
print(f"Quantidade de zeros: {zeros}")