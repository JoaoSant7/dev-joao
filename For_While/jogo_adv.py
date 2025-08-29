# Jogo de adivinhação
secreto = 42
palpite = None

while palpite != secreto:
    palpite = int(input("Adivinhe o número secreto: "))

    if palpite < secreto:
        print("Muito baixo! Tente novamente.")
    elif palpite > secreto:
        print("Muito alto! Tente novamente.")

print("Parabéns! Você acertou o número secreto.")
