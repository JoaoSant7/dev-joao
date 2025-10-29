from dataclasses import dataclass, field
from typing import Optional, List
from uuid import uuid4


# -----------------------------
# MODELO: COMBO
# -----------------------------
@dataclass(frozen=True)
class Combo:
    pipoca: Optional[str] = None
    bebida: Optional[str] = None
    chocolate: bool = False
    extras: List[str] = field(default_factory=list)
    preco_total: float = 0.0

    def __str__(self):
        itens = []
        if self.pipoca:
            itens.append(f"Pipoca ({self.pipoca})")
        if self.bebida:
            itens.append(f"Bebida ({self.bebida})")
        if self.chocolate:
            itens.append("Chocolate")
        if self.extras:
            itens.extend(self.extras)
        desc = ", ".join(itens) if itens else "Combo vazio"
        return f"{desc} — Total: R${self.preco_total:.2f}"


# -----------------------------
# BUILDER: COMBOBUILDER
# -----------------------------
class ComboBuilder:
    PRECOS_PIPOCA = {"pequena": 10.0, "média": 15.0, "grande": 20.0}
    PRECOS_BEBIDA = {"água": 5.0, "coca": 8.0, "guaraná": 7.0}
    PRECO_CHOCOLATE = 6.0
    PRECOS_EXTRAS = {"nachos": 12.0, "molho extra": 3.0, "balas": 4.0}

    def __init__(self):
        self._reset()

    def _reset(self):
        self._pipoca = None
        self._bebida = None
        self._chocolate = False
        self._extras = []
        self._preco_total = 0.0
        return self

    def add_pipoca(self, tamanho: str):
        if tamanho not in self.PRECOS_PIPOCA:
            raise ValueError("Tamanho de pipoca inválido.")
        self._pipoca = tamanho
        self._preco_total += self.PRECOS_PIPOCA[tamanho]
        return self

    def add_bebida(self, tipo: str):
        if tipo not in self.PRECOS_BEBIDA:
            raise ValueError("Tipo de bebida inválido.")
        self._bebida = tipo
        self._preco_total += self.PRECOS_BEBIDA[tipo]
        return self

    def add_chocolate(self, com: bool = True):
        self._chocolate = com
        if com:
            self._preco_total += self.PRECO_CHOCOLATE
        return self

    def add_extra(self, item: str):
        if item not in self.PRECOS_EXTRAS:
            raise ValueError("Extra inválido.")
        self._extras.append(item)
        self._preco_total += self.PRECOS_EXTRAS[item]
        return self

    def get_combo(self, reset_builder: bool = True) -> Combo:
        combo = Combo(
            pipoca=self._pipoca,
            bebida=self._bebida,
            chocolate=self._chocolate,
            extras=list(self._extras),
            preco_total=round(self._preco_total, 2),
        )
        if reset_builder:
            self._reset()
        return combo


# -----------------------------
# PEDIDO
# -----------------------------
@dataclass
class Pedido:
    combos: List[Combo] = field(default_factory=list)
    pedido_id: str = field(default_factory=lambda: str(uuid4()))

    @property
    def total(self) -> float:
        return round(sum(c.preco_total for c in self.combos), 2)

    def adicionar_combo(self, combo: Combo):
        self.combos.append(combo)

    def __str__(self):
        texto = [f"\nPedido #{self.pedido_id[:8]}:"]
        for i, combo in enumerate(self.combos, start=1):
            texto.append(f"  Combo {i}: {combo}")
        texto.append(f"\nTotal do pedido: R${self.total:.2f}\n")
        return "\n".join(texto)


# -----------------------------
# INTERFACE DE MENU
# -----------------------------
def menu_interativo():
    pedido = Pedido()
    builder = ComboBuilder()

    while True:
        print("\nMONTAGEM DE COMBO")
        print("1. Escolher pipoca")
        print("2. Escolher bebida")
        print("3. Adicionar chocolate")
        print("4. Adicionar extra")
        print("5. Finalizar combo")
        print("6. Ver pedido atual")
        print("0. Finalizar pedido e sair")

        opcao = input("Escolha uma opção: ").strip()

        try:
            if opcao == "1":
                print("\nTamanhos disponíveis:", list(builder.PRECOS_PIPOCA.keys()))
                t = input("Escolha o tamanho da pipoca: ").lower().strip()
                builder.add_pipoca(t)
                print("Pipoca adicionada!")

            elif opcao == "2":
                print("\nBebidas disponíveis:", list(builder.PRECOS_BEBIDA.keys()))
                b = input("Escolha a bebida: ").lower().strip()
                builder.add_bebida(b)
                print("Bebida adicionada!")

            elif opcao == "3":
                c = input("Deseja chocolate? (s/n): ").lower().strip()
                builder.add_chocolate(c == "s")
                print("Chocolate adicionado!" if c == "s" else "Sem chocolate.")

            elif opcao == "4":
                print("\nExtras disponíveis:", list(builder.PRECOS_EXTRAS.keys()))
                e = input("Digite o nome do extra: ").lower().strip()
                builder.add_extra(e)
                print("Extra adicionado!")

            elif opcao == "5":
                combo = builder.get_combo()
                pedido.adicionar_combo(combo)
                print("\nCombo finalizado com sucesso:")
                print(combo)

            elif opcao == "6":
                print(pedido)

            elif opcao == "0":
                print("\nPedido finalizado!")
                print(pedido)
                break

            else:
                print("Opção inválida, tente novamente.")

        except Exception as e:
            print("Erro:", e)


# -----------------------------
# EXECUÇÃO
# -----------------------------
if __name__ == "__main__":
    menu_interativo()
