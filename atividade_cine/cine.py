idade = int(input('Digite a sua idade:'))
estudante = (input('Você é estudante?'))
if idade >= 12 :
    if estudante == 's':
        print('Preço estudante: R$15,00')
    else:
        print('Preço normal: R$30,00')
else:
    print('Preço infantil: R$15,00')
