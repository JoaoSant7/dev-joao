# Cadastro e análise de idades
idades = []

while True:
    idade = int(input("Digite uma idade (ou 0 para parar): "))
    if idade == 0:
        break
    idades.append(idade)

maiores = 0
for idade in idades:
    if idade >= 18:
        maiores += 1

print(f"Foram digitadas {len(idades)} idades.")
print(f"{maiores} pessoa(s) são maiores de idade.")
