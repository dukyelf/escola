'''# Questão Azul

termo = int(input("Insira o primeiro termo -- "))
razao = int(input("Insira a razão -- "))
quanttermos = int(input("Insira o número de termos -- "))

def calcular_pa(termo, razao, quant):
    listatermos = []
    for i in range(quant):
        listatermos.append(termo)
        termo = termo + razao
    return listatermos

retorno = calcular_pa(termo, razao, quanttermos)
print(retorno)

# Questão Laranja

termosfibo = int(input("FIBONACCI \nInsira a quantidade de termos que você deseja gerar -- "))

def fibonacci(termos):
    listafibo = []
    n1 = 0
    n2 = 1
    n3 = 0
    for i in range(termos):
        listafibo.append(n3)
        n1 = n2+n3
        n2 = n3
        n3 = n1
    return listafibo

retornofibo = fibonacci(termosfibo)
print(retornofibo)

# Questão Rosa

def validar_emails(lista_emails):
    emails_validos = []
    for email in lista_emails:
        if email.count("@") == 1 and email.count(" ") == 0:
            email_separado = email.split("@") 
            if email_separado[1].count(".") == 1:
                emails_validos.append(email)
        
    return emails_validos
emails = []
for i in range(5):
    emails.append(input("Insira o email -- "))

print(f"--- Emails válidos ---\n {validar_emails(emails)}")
'''
# Questão Branca

listanotas = []
quantnotas = int(input("Insira a quantidade de notas que deseja inserir -- "))

for i in range(quantnotas):
    listanotas.append(float(input(f"Insira a {i+1}ª nota (De 0 a 100) -- ")))

print("Notas numéricas:", listanotas)

def nota_para_conceito(lista_de_notas, quantidade_de_notas):
    listaconceitos = []
    for nota in lista_de_notas:
        if nota >= 0 and nota < 60:
            listaconceitos.append("F")
        elif nota >= 60 and nota < 70:
            listaconceitos.append("D")
        elif nota >= 70 and nota < 80:
            listaconceitos.append("C")
        elif nota >= 80 and nota < 90:
            listaconceitos.append("B")
        elif nota >= 90 and nota <= 100:
            listaconceitos.append("A")
        else:
            return "Há nota(s) fora da escala!"
    return listaconceitos

resultado = nota_para_conceito(listanotas, quantnotas)
print(resultado)
        
