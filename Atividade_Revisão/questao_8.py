# Programa: Controle de Despesas

despesas = []
print("=== Controle de Despesas ===")
print("Digite os valores das despesas. Digite 0 para encerrar.\n")

while True:
    valor = float(input("Digite uma despesa: R$ "))
    if valor == 0:
        break
    if valor < 0:
        print("Valor inválido! Digite apenas números positivos.")
    else:
        despesas.append(valor)

if len(despesas) > 0:
    total = sum(despesas)
    qtd = len(despesas)
    media = total / qtd

    print("\nResumo das despesas:")
    print(f"1. Total gasto: R$ {total:.2f}")
    print(f"2. Número de despesas: {qtd}")
    print(f"3. Valor médio por despesa: R$ {media:.2f}")
else:
    print("\nNenhuma despesa registrada.")
