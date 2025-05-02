aluno = {
    "ID":1,
    "Nome":"Matheus",
    "Idade":17,
    "Notas":[]
}

for i in range(3):
    aluno["Notas"].append(float(input("Insira uma nota -- ")))

print(aluno)
print(aluno["ID"])

print(aluno["Nome"])
for nota in aluno["Notas"]:
    print(nota)