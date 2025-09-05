while True:
    nome = input("Digite o seu nome completo: ")
    if len(nome.replace(" ", "")) < 4:
        print("Seu nome deve possuir pelo menos 4 letras. Por favor, tente novamente.")
    else:
        break

while True:
    try:
        idade = int(input("Digite a sua idade(entre 1 e 100 anos): "))
        if idade <= 0 or idade > 100:
            print("Idade inválida. Digite uma idade entre 0 a 100.")
        else:
            break
    except ValueError:
        print("Digite um número para a idade.")



while True:
    try:
        salario = float(input("Digite o seu salário: "))
        if salario < 0:
            print("Seu salário não pode ser menor do que 0 reais")
        else:
            break
    except ValueError:
        print("Você não pode digitar seu salário por extenso")


while True:
    try:
        genero = str(input( """
Qual o seu gênero?

[ m ] Masculino 
[ f ] Feminino
[ o ] Outro
""")).upper().strip()

        if genero in ['M', 'F', 'O']:
            break
        else:
            print("Você deve escolher uma das três opções de gênero (m, f ou ).")

    except ValueError:
        print("Entrada inválida. Por favor, tente novamente.")

while True:
    try:
        emprego = str(input( """
Informe a sua situação empregatícia?

[ e ] empregado
[ d ] desempregado
[ a ] autônomo""")).upper().strip()

        if emprego in ['E', 'D', 'A']:
            break
        else:
            print("Você deve escolher uma das três opções de gênero (e, d ou a)")
    except ValueError:
        print("Entrada inválida. Por favor, tente novamente.")

print("\n--- Dados Coletados ---")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R${salario:.2f}")
print(f"Gênero: {genero}")
print(f"Situação Empregatícia: {emprego}")
