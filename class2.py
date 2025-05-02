class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.estado = False
    
    def ligar(self):
        self.estado = True
        print(f"O carro {self.modelo} foi ligado!")

    def desligar(self):
        self.estado = False
        print(f"O carro {self.modelo} foi desligado!")

    def info(self):
        aux = "Ligado" if self.estado else "Desligado"
        print("-" * 45)
        print(" -- Informações do Carro -- ")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Estado: {aux}")

carros = []

while True:
    print("\n               MENU - LOCADORA\n")
    print("1 -- Cadastrar um novo carro")
    print("2 -- Ligar carro")
    print("3 -- Desligar carro")
    print("4 -- Ver carros disponíveis")
    print("5 -- Sair")

    opcao = int(input("Escolha uma opção de 1 à 5 -- "))
    if opcao == 1:
        marca = str(input("Insira a marca -- "))
        modelo = str(input("Insira o modelo -- "))
        ano = int(input("Insira o ano -- "))
        carro = Carro(marca, modelo, ano)
        carros.append(carro)
        print(f"O carro {marca} {modelo} foi cadastrado com sucesso!")
    elif opcao == 2:
        modelo = input("Qual é o modelo do carro que você deseja ligar? -- ")
        for i in carros:
            if i.modelo == modelo:
                carro.ligar()
                break
            else:
                print("Carro não encontrado!")