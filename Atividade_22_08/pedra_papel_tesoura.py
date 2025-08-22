import random

opcoes = ["pedra", "papel", "tesoura"]

usuario = input("Escolha pedra, papel ou tesoura: ").lower()

computador = random.choice(opcoes)

print(f"\nVocê escolheu: {usuario}")
print(f"O computador escolheu: {computador}")

if usuario == computador:
    print("Empate!")
elif (usuario == "pedra" and computador == "tesoura") or \
     (usuario == "tesoura" and computador == "papel") or \
     (usuario == "papel" and computador == "pedra"):
    print("Você venceu!")
elif usuario in opcoes:
    print("O computador venceu!")
else:
    print("Opção inválida. Escolha apenas pedra, papel ou tesoura.")
