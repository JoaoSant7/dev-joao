try:
    numero = int(input("Digite um número inteiro: "))
    
    # Números menores ou iguais a 1 não são primos
    #Um número primo é um número natural maior que 1 que tem apenas dois divisores positivos: o número 1 e ele mesmo
    if numero <= 1:
        print(f"O número {numero} não é primo.")
    else:
        eh_primo = True  # Assume que o número é primo
        for i in range(2, numero):
            if numero % i == 0:
                eh_primo = False  # Se for divisível, não é primo
                break
        
        if eh_primo:
            print(f"O número {numero} é primo.")
        else:
            print(f"O número {numero} não é primo.")
            
except ValueError:
    print("Entrada inválida. Por favor, digite apenas números inteiros.")