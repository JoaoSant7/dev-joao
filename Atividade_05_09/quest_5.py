while True:
    try:
        cidade_a = int(input("Digite o número de habitantes da cidade 'a': "))
        taxa_a = float(input("Digite a taxa de crescimento da cidade 'a': "))
        cidade_b = int(input("Digite o número de habitantes da cidade 'b': "))
        taxa_b = float(input("Digite a taxa de crescimento da cidade 'b': "))

        if cidade_a > 0 and taxa_a > 0 and cidade_b > 0 and taxa_b > 0:
            print("Valores válidos! Prosseguindo com o cálculo...")
            break
        else:
            print("Erro: Todos os valores devem ser positivos. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números.")

anos = 0

while cidade_a <= cidade_b:
    cidade_a += cidade_a * taxa_a
    cidade_b += cidade_b * taxa_b
    anos += 1

print(f"\nSerão necessários {anos} anos para que a população da cidade A ultrapasse a da cidade B.")
print(f"População final da cidade A: {int(cidade_a)}")
print(f"População final da cidade B: {int(cidade_b)}")