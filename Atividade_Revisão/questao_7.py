# Programa: Simulador de interruptor de luz

luz_acesa = False  # estado inicial

while True:
    print("\nO que fazer?")
    print("1: Apertar interruptor")
    print("0: Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        luz_acesa = not luz_acesa  # inverte o estado da luz
        if luz_acesa:
            print("A luz está ACESA.")
        else:
            print("A luz está APAGADA.")
    elif opcao == "0":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida! Tente novamente.")
