class Animais:
    def __init__(self, nome=None, cobertura=None, raca=None):
        self.nome = nome
        self.cobertura = cobertura
        self.raca = raca

    def dar_nome(self, nome=None):
        self.nome = nome


class Cachorros(Animais):
    def trocar(self, cobertura=None, raca=None):
        self.cobertura = "Crespo"
        self.raca = "Pitbull"


animais = Animais()
cachorros = Cachorros(cobertura="Lisa", raca="Pintcher")
animais.dar_nome("Rex")
print("Nome: ", animais.nome)
print("Cachorro: ", cachorros.cobertura)
print("Raça: ", cachorros.raca)
cachorros.trocar()
print("Cachorro: ", cachorros.cobertura)
print("Raça: ", cachorros.raca)
