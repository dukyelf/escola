# Questão Verde

vendedor = {}
nomevendedor = input("Insira o nome do vendedor -- ")
vendedor[nomevendedor] = []
def calcular_total_vendas(vendedor):
    for i in range(5):
        vendedor[nomevendedor].append(float(input(f"Insira o valor da {i+1}ª venda semanal -- ")))

    for vende in vendedor.keys():
        print(f"Vendedor - {vende} \nVendas - R$ {sum(vendedor[vende]):.2f}")
calcular_total_vendas(vendedor)

# Questão Verde-limão

quantalunos = int(input("Insira a quantidade de alunos que você quer cadastrar"))
alunos = {}
for i in range(quantalunos):
    nomealuno = input(f"Insira o nome do {i+1}º aluno -- ")
    alunos[nomealuno] = []
    for i in range(3):
        alunos[nomealuno].append(float(input(f"Insira a {i+1}ª nota")))
def calcular_medias():
    media = []
    for chave in alunos.keys():
        media.append(sum(alunos[chave]) / len(alunos[chave]))
    print("ALUNOS:")
    for chave in alunos.keys():
        print(chave)
    print("As suas médias foram","-" *45)
    print(media)
calcular_medias()