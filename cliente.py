class Cliente:
    #construtor + atributos

    def __init__(self, nome, cpf, tel, email, endereco):
        self.nome=nome
        self.cpf=cpf
        self.__Telefone=tel
        self.email=email
        self.endereco=endereco

    # encapsulamento (analizar se precisa)

    def getTelefone(self):
        return self.__Telefone

    def setTelefone(self, tel):
        self.__Telefone=tel

    #metodos - acoes#

    def imprimeficha(self):
        print(f"\n------------------ CLIENTE--------------------"
              f"\nNOME: {self.nome} "
              f"\nENDERECO: {self.endereco}"
              f"\nCPF: {self.cpf}"
              f"\nEMAIL: {self.email}"
              f"\nTELEFONE: {self.__Telefone}"
              f"\n----------------------------------------------"
              )
