class Pato:
    # 1. Atributo de CLASSE: Compartilhado por todas as instâncias (Patos)
    especie = "Anas platyrhynchos (Pato-real)"

    # Método Construtor (__init__): Define os atributos de INSTÂNCIA
    def __init__(self, cor, idade):
        self.cor = cor  # Atributo de instância
        self.idade = idade  # Atributo de instância

    # 1. Método: nadar
    def nadar(self):
        # O método usa um atributo para personalizar a saída
        return f"O pato {self.cor} está deslizando calmamente na água."

    # 2. Método: voar
    def voar(self):
        # O método usa um atributo para personalizar a saída
        if self.idade >= 1:
            return f"O pato ({self.idade} anos) abriu as asas e está voando para o sul."
        else:
            return "O pato é muito jovem para voar longas distâncias."


# --- Demonstração ---

# 1. Criação de um objeto Pato
pato_donald = Pato("branco", 4)

# 2. Acessando os ATRIBUTOS
print(f"Cor do pato: {pato_donald.cor}")
print(f"Espécie do pato: {Pato.especie}")
print("-" * 25)

# 3. Chamando os MÉTODOS
print(f"Ação 1: {pato_donald.nadar()}")
print(f"Ação 2: {pato_donald.voar()}")
