carros = {"Marca": "Chevrolet"}
print(carros.get("Marca"))
carros["Marca"] = "Fiat"
print(carros["Marca"])

funcionario = {"12345678":
              {"nome": "Matheus", "idade": 27, "cidade": "liubliu"},
               "12345677": 
              {"nome": "Matheus2", "idade": [272, 455, 456], "cidade": "liubliu2"}}

print(funcionario["12345677"]["nome"])


for chave in funcionario["12345677"].keys():
    print(chave)

cpf = input("Informe o CPF -- ")
if cpf in funcionario:
    print(f"O nome do funcionário é {funcionario[cpf]["nome"]}")
else:
    print("Funcionário não encontrado")
