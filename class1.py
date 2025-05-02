class Cliente:
    def __init__(self, nome, telefone):

        self.nome = nome
        self.telefone = telefone
    
    def info(self):
        print("-- Informações do Cliente --")
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")

nome = input("Qual é o seu nome? - ")
telefone = int(input("Qual é o seu número de telefone? - "))
c1 = Cliente(nome, telefone)
print(" -- ")
c1.info()
print(" -- ")

