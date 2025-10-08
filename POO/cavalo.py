class Cavalo:
    raca = "Mustang"

    def __init__(self, cor, idade):
        self.cor = cor
        self.idade = idade

    def correr(self):
        return f"O cavalo de {self.cor} corre velozmente!"

    def trotar(self):
        if self.idade >= 1:
            return f"O cavalo de {self.idade} anos trota graciosamente."
        else:
            return "O cavalo é muito jovem para trotar graciosamente."


cavalo_mustang = Cavalo("baio", 3)

print(f"Cor do cavalo: {cavalo_mustang.cor}")
print(f"Raça do cavalo: {Cavalo.raca}")
print("-" * 25)


print(f"Ação 1: {cavalo_mustang.correr()}")
print(f"Ação 2: {cavalo_mustang.trotar()}")
