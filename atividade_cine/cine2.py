total_ingressos = 0
valor_total_arrecadado = 0

while True:
    try:
        idade = int(input('Digite a idade do cliente: '))
        
        preco = 0
        if idade >= 12:
            estudante = input('Você é estudante? (s/n): ').lower()
            if estudante == 's':
                preco = 15.00
                print('Preço estudante: R$15,00')
            else:
                preco = 30.00
                print('Preço normal: R$30,00')
        else:
            preco = 15.00
            print('Preço infantil: R$15,00')
            
        
        total_ingressos += 1
        valor_total_arrecadado += preco
            
        
        while True:
            novo_cliente = input('\nDeseja registrar um novo cliente? (s/n): ').lower()
            if novo_cliente == 's':
                break  
            elif novo_cliente == 'n':
                print('\nFim do expediente.')
                print(f'Total de ingressos vendidos: {total_ingressos}')
                print(f'Valor total arrecadado: R${valor_total_arrecadado:.2f}')
                exit() 
            else:
                print('Entrada inválida. Digite s (para sim) ou n (para não).')

    except ValueError:
        print('Entrada inválida. Por favor, digite um número para a idade.')