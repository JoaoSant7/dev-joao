cardapio = {
    1: ("Hambúrguer", 15.00),
    2: ("Batata Frita", 5.00),
    3: ("Refrigerante", 6.00),
    4: ("Milkshake", 10.00),
    5: ("Açaí", 10.00)
}

print(" *** Cardápio *** ")
for codigo, (item, preco) in cardapio.items():
    print(f"{codigo} - {item} - R${preco:.2f}")

pedidos = [] 

while True:
    try:
        escolha = int(input("\nDigite o número do item desejado (0 para finalizar): "))

        if escolha == 0:
            break
        elif escolha in cardapio:
            item, preco = cardapio[escolha]
            pedidos.append((item, preco))
            print(f"Adicionado: {item} - R${preco:.2f}")
        else:
            print("Opção inválida.")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

# Mostra o resumo final
if pedidos:
    print("\n=== Seu Pedido ===")
    total = 0
    for item, preco in pedidos:
        print(f"- {item} - R${preco:.2f}")
        total += preco
    print(f"\nTotal a pagar: R${total:.2f}")
else:
    print("\nNenhum item selecionado.")
