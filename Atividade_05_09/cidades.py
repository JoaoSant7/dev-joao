cidade_a = 90000
taxa_a = 3.5

cidade_b = 250000
taxa_b = 1.2

anos = 0

while cidade_a <= cidade_b:
    cidade_a += cidade_a * taxa_a
    cidade_b += cidade_b * taxa_b
    anos += 1

print(f"Serão necessários {anos} anos para que a população da cidade A ultrapasse a da cidade B.")
print(f"População final da cidade A: {int(cidade_a)}")
print(f"População final da cidade B: {int(cidade_b)}")