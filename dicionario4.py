dicionario_vazio = {}
dicionario = {"nome": "Matheus", "idade": 25, "cidade": "São Paulo"}

print(dicionario["nome"])
print(dicionario.get("idade"))

dicionario["profissão"] = "Engenheiro"
dicionario["cidade"] = "RJ"

del dicionario["idade"]
print(dicionario)

valor_removido = dicionario.pop("cidade")
print(valor_removido)

elemento = dicionario.popitem()
print(elemento)

for chave in dicionario.keys():
    print(chave)

for valor in dicionario.values():
    print(valor)

for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")

if "nome" in dicionario:
    print("A chave 'nome' existe no dicionário.")

dicionario.clear()
dicionario_copia = dicionario.copy()

outro_dicionario = {"pais": "Brasil", "idade": 30}

dicionario.update(outro_dicionario)
print(dicionario)