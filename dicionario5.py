funcionario = {"Nome": [] , 'Salario':[] }

quantfuncionarios = int(input("Quantos funcionários você quer cadastrar? -- "))

for i in range(quantfuncionarios):
    funcionario["Nome"].append(input("Insira o nome do funcionário -- "))

for i in range(quantfuncionarios):
    funcionario["Salario"].append(float(input("Insira o salário -- ")))

for chave, valor in funcionario.items():
    print(f"{chave}: {valor:}")

mediasalarial = sum(funcionario["Salario"]) / len(funcionario["Salario"])
print(f"Média dos salários: {mediasalarial:.2f}")

nome_func = input("Insira o nome do funcionário a ser encontrado -- ")

if nome_func in funcionario["Nome"]:
    pesquisa = funcionario["Nome"].index(nome_func)
    print(f"Funcionário encontrado: {nome_func}")
    print(f"Salário: {funcionario["Salario"][pesquisa]:.2f}")
else:
    print("Funcionário não encontrado")