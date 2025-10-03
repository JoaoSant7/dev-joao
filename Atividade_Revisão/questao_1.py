def votacao():
    # Dicionário
    votos_validos = {
        10: "Candidato A",
        20: "Candidato B",
        30: "Candidato C",
        98: "Voto Nulo",
        99: "Voto em Branco",
    }

    while True:
        try:
            voto = int(
                input("Digite seu voto (10-A, 20-B, 30-C, 98-Nulo, 99-Branco): ")
            )
            if voto in votos_validos:
                print(f"Voto registrado: {votos_validos[voto]}")
                break
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")


# Executar o programa
votacao()
