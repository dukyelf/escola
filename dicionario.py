aluno = {
    "ID":1,
    "Nome":"Matheus",
    "Idade":17,
    "Notas":[5, 7, 4, 9, 9, 9, 8.7, 7]
}

print(aluno.values())
for i, v in aluno.items():
    print("Chave:", i, "Valor:", v)