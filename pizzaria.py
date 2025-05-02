

print("-" *45)
print("Seja bem-vindo a pizzaria!")
print("-" *45)

valor = []
print("1 - Queijo: R$ 15")
print("2 - Pepperoni: R$ 20")
print("3 - Vegetariana: R$ 18")

pizza = int(input("Insira a pizza que você quer -- "))
if pizza == 1:
    valor.append(15)
elif pizza == 2:
    valor.append(20)
elif pizza == 3:
    valor.append(18)
else:
    print("Pizza não encontrada!")
    sys.exit()

print("-" *45)
print("1 -- Cogumelos: R$ 2 por unidade")
print("2 -- Azeitonas: R$ 1 por unidade")
print("3 -- Pimentão: R$ 1.5 por unidade")
print("4 -- Extra queijo: R$ 3 por unidade")
print("-" *45)

quantingredientes = int(input("Você quer quantos ingredientes? -- "))
if quantingredientes == 0:
    valortotal = sum(valor)
    print(f"O valor total foi R${valortotal:.2f}")
    sys.exit()

if quantingredientes > 4:
    print("Você só pode escolher 4 ingredientes")
    sys.exit()

print("-" *45)

for i in range(quantingredientes):
    ingrediente = int(input(f"Insira o {i+1}º ingrediente -- "))
    contingrediente = int(input("Quantos? -- "))
    if ingrediente == 1:
        valor.append(2*contingrediente)
    elif ingrediente == 2:
        valor.append(1*contingrediente)
    elif ingrediente == 3:
        valor.append(1.5*contingrediente)
    elif ingrediente == 4:
        valor.append(3*contingrediente)
    else:
        print("Ingrediente não encontrado!")
        sys.exit()

print("-" *45)

valortotal = sum(valor)
print(f"O total foi R${valortotal:.2f}")

print("-" *45)