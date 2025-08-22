usuario_registrado = "admin"
senha_registrada = "WinRad10"

usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

if usuario == usuario_registrado and senha == senha_registrada: 
    print("Acesso concedido!") 
else:
    print("Acesso negado!")