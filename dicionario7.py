import sys

# Questão 1

dic = {}

qntd = int(input("Quantos produtos serão cadastrados?: "))

for i in range(qntd):
    nome = input("Insira o nome do produto: ")
    quantidade = int(input("Insira a quantidade: "))
    dic[nome] = quantidade

for chave, valor in dic.items():
    print(f"Produto: {chave} | Estoque: {valor}")

nome_prod = input("Insira o nome do produto para ser encontrado: ")
if nome_prod in dic:
    print(f"O produto {nome_prod} foi encontrado!")
    print(f"Estoque: {dic[nome_prod]}")

else:
    print("Não encontrado!!")
    sys.exit()

prod_att = input("Insira o nome do produto a ser atualizado: ")  
 
if prod_att in dic:
    cond = input("Você quer adicionar ou remover? (a/r) -- ")
    if cond.lower() == 'a':
        qntd_mais = int(input("Insira a quantidade a ser adicionada -- "))
        dic[prod_att] += qntd_mais
        print(f"Após adição {prod_att} ficou com {dic[prod_att]} quantidades")

    elif cond.lower() == 'r':
        qntd_menos = int(input("Insira a quantidade a ser removida -- "))
        if qntd_menos <= dic[prod_att]:    
            dic[prod_att] -= qntd_menos
            print(f"Após a remoção {prod_att} ficou com {dic[prod_att]}")
        else:
            print("Quantidade a ser removida maior que a quantidade existente")
    else:
        print("Resposta invalida!") 
else:
    print("Produto não encontrado!")

# Questão 2 -- 

alunos = {}

quantalunos = int(input("Quantos alunos você deseja cadastrar? -- "))

for i in range(quantalunos):
    aluno = input(f"Insira o nome do {i+1}º aluno -- ")
    nota = float(input("Insira a nota (de 1 a 10) -- "))
    if nota < 0 or nota > 10:
        print("A nota tem que ser de 1 a 10")
        sys.exit()
    alunos[aluno] = nota


print("--- Alunos e Notas ---")
for chave, valor in alunos.items():
    print(f"{chave} -- {valor}")

buscaaluno = input("Insira o nome do aluno que você deseja procurar -- ")
if buscaaluno in alunos:
    print(f"O aluno {buscaaluno} foi encontrado!")
    print(f"A nota do aluno {buscaaluno} é {alunos[buscaaluno]}")
else:
    print(f"O aluno {buscaaluno} não foi encontrado")

maior_nota = max(alunos.values())
menor_nota = min(alunos.values())
media = sum(alunos.values()) / len(alunos)
print(f"A maior nota é {maior_nota}")
print(f"A menor nota é {menor_nota}")
print(f"A média da turma é {media}")

# Questão 3

filmes = {}

quantfilmes = int(input("Quantos filmes você deseja cadastrar? -- "))
for i in range(quantfilmes):
    filme = input(f"Qual é o nome do {i+1}º filme? -- ")
    ano = int(input("Qual é o ano do filme? -- "))
    filmes[filme] = ano

print("Filmes")
for chave, valor in filmes.items():
    print(f"{chave} -- {valor}")

buscafilme = input("Insira o nome do filme que você deseja procurar -- ")
if buscafilme in filmes:
    print(f"O filme {buscafilme} foi encontrado!")
    print(f"Ano -- {filmes[buscafilme]}")
else:
    print(f"O filme {buscafilme} não está no catálogo")
buscaano = int(input("Insira o ano do filme -- "))
listafilmesano = []
if buscaano in filmes.values():
    for nomefilme, ano in filmes.items():
        if ano >= buscaano:
            listafilmesano.append(nomefilme)
    if nomefilme:
        for nome in listafilmesano:
            print(nome)
    else:
        print("Filme não encontrado")

# Quarta questão

listaproj = {}
quantprojetos = int(input("Quantos projetos você deseja cadastrar -- "))
projeto = {}
for i in range(quantprojetos):
    nomeproj = input("Insira o nome do projeto -- ")
    responsavel = input("Responsável? -- ")
    horas = int(input("Quantas horas? -- "))
    status = input("Ativo ou Inativo? -- ")
    listaproj[nomeproj] = {
    "Responsável" : responsavel, "Horas" : horas, "Status": status
    }

print(listaproj)

menu = int(input("1 - Listar todos os projetos \n2 - Buscar projetos por responsável \n3 - Exibir somente projetos ativos \n4 - Calcular total de horas estimadas \n5 - Alterar o status de um projeto \n6 - Sair \n-- "))
while menu != 6:
    if menu == 0:
       menu = int(input("1 - Listar todos os projetos \n2 - Buscar projetos por responsável \n3 - Exibir somente projetos ativos \n4 - Calcular total de horas estimadas \n5 - Alterar o status de um projeto \n6 - Sair \n-- "))
    if menu == 1:
        print(f"Todos os projetos são: {list(listaproj.keys())}")
        menu = 0
    if menu == 2:
        buscaproj = input("Insira o nome do responsavel: ")
        projetos_responsavel = []
        for nome, dicmenor in listaproj.items():
            if dicmenor['Responsável'] == buscaproj:
                projetos_responsavel.append(nome)
        if projetos_responsavel:
            print(f"Os projetos que {buscaproj} está encarregado são esses: {','.join(projetos_responsavel)}")      
        else:
            print(f"Este responsável não participa de nenhum projeto!")
        menu = 0   
    if menu == 3:
        projetos_ativos = []
        for nome, dicmenor in listaproj.items():
         if dicmenor['Status'] == 'Ativo' or dicmenor['Status'] == 'ativo':
            projetos_ativos.append(nome)
        if projetos_ativos:
         print(f"Os Projetos que estão ativos são esses: {', '.join(projetos_ativos)}")
        else:
            print("Nenhum projeto ativo no momento!")
        menu = 0
    if menu == 4:
        horas_total = 0
        for dicmenor in listaproj.values():
         horas_total+=dicmenor['Horas']
        print(f"Todos os projetos tem {horas_total} horas!")
        menu = 0
    if menu == 5:
        buscaproj = input('Insira o nome do projeto para ser alterado: ')
        if buscaproj in listaproj:
            alterar_status = input("Insira o novo status do projeto: ")
            listaproj[buscaproj]['Status'] = alterar_status
            print(f"O status do projeto {buscaproj} foi alterado para {alterar_status}")
        else:
         print("Projeto não encontrado!")
        menu = 0
    if menu >= 7 or menu < 0:
       print("Opção não disponível!")
       menu = 0
print("Programa encerrando...")
