lista = ["Casa", "Carro", "Geladeira"]
print(lista)
lista.append("Fogão") # Adiciona um item no final da lista
print(lista)
lista.sort() # Organiza em ordem crescente
print(lista)
lista.insert(0, "Matheus") # Insere um item em determinada posição
print(lista)
lista.pop(3) # Remove um elemento via posição; O último elemento será removido se não tiver nada por padrão
print(lista)
lista.remove("Casa") # Remove um elemento via valor
print(lista)
nome = input("Você quer procurar qual nome? -- ")
quantidade = (lista.count(nome)) # Conta quantas vezes um elemento aparece
print(f"A quantidade de vezes que {nome} aparece na lista é {quantidade}.")
lista.reverse() # Organiza em reverso
print(*lista)
lista2 = lista.copy() # Cria uma cópia da lista
lista.clear() # Esvazia a lista
print(lista)
print(*lista2)