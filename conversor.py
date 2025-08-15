cotacao_dolar = 5.25

valor_real = float(input("Digite o valor em reais que você deseja converter: "))

valor_dolares = valor_real / cotacao_dolar

print(f"Valor em reais: R$ {valor_real:.2f}")
print(f"Valor em dólares: US$ {valor_dolares:.2f}")
