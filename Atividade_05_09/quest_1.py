positivo = [1,2,3,4,5]

while True:

    nota = int(input("Nos dê uma nota de 0 a 5:"))
    if nota in positivo:
        print(f"Obrigado pela sua avaliação com nota {nota}!")
    else:
        print("Valor inválido, digite um número válido (0 a 5)")