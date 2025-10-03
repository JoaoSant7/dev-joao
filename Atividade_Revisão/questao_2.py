def main():
    # Lista de produtos
    produtos = {
        1: ("Biscoito", 3.50),
        2: ("Bolacha", 2.75),
        3: ("Manteiga", 3.90),
        4: ("Fubá", 3.00),
        5: ("Miojo", 1.80),
    }

    total = 0.0

    print("=== Caixa de Supermercado ===")

    while True:
        print("\n--- Lista de Produtos ---")
        for codigo, (nome, preco) in produtos.items():
            print(f"{codigo} - {nome} (R$ {preco:.2f})")
        print("0 - Finalizar compra")

        try:
            escolha = int(input("Escolha o produto: "))
        except ValueError:
            print("Digite apenas números!")
            continue

        if escolha == 0:
            break
        elif escolha in produtos:
            nome, preco = produtos[escolha]
            try:
                qtd = int(input(f"Quantas unidades de {nome}? "))
            except ValueError:
                print("Quantidade inválida.")
                continue

            if qtd <= 0:
                print("Quantidade deve ser positiva!")
                continue

            subtotal = preco * qtd
            total += subtotal
            print(f"Adicionado: {qtd} x {nome} = R$ {subtotal:.2f}")
        else:
            print("Opção inválida, tente novamente.")

    print("\n=== COMPRA FINALIZADA ===")
    print(f"Total a pagar: R$ {total:.2f}")


if __name__ == "__main__":
    main()
