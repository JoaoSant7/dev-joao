usuario = str(input("Digite o seu nome de usuário:"))
senha = str(input("Digite a sua senha:"))

if usuario in senha:
    print(f"Seu nome de usuário não pode estar incluído em sua senha!")
else:
    print(f"Bem vindo, {usuario}! Sua senha é: {senha}!")