aluno = {
    "Nome":[],
    "Nota1":[],
    "Nota2":[],
    "Nota3":[]
}

for i in range(3):
    aluno["Nome"].append(input(f"Insira o {i+1}º nome  -- "))

print(aluno["Nome"])

for i in range(2):
    aluno["Nota1"].append(float(input(f"Insira a {i+1}ª nota para {aluno["Nome"][0]} -- ")))

for i in range(2):
    aluno["Nota2"].append(float(input(f"Insira a {i+1}ª nota para {aluno["Nome"][1]} -- ")))

for i in range(2):
    aluno["Nota3"].append(float(input(f"Insira a {i+1}ª nota para {aluno["Nome"][2]} -- ")))

media1 = sum(aluno["Nota1"]) / len(aluno["Nota1"])
media2 = sum(aluno["Nota2"]) / len(aluno["Nota2"])
media3 = sum(aluno["Nota3"]) / len(aluno["Nota3"])

print(f"As médias dos alunos {aluno["Nome"][0]}, {aluno["Nome"][1]} e {aluno["Nome"][2]} são")
print(f" -- {media1}, {media2} e {media3}. --")