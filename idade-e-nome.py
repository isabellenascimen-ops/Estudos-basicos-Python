# começo com um input classificando o nome

nome = input("Qual é seu nome? ")

# uso nome.isalpha() para espeficar que não pode inserir numeros

while not nome.isalpha():
    print("Porfavor, digite apenas caracteres. ")
    nome = input ("Qual é seu nome? ")

# logo ele mostra uma apresentação mais o nome inserido

print("Prazer, " + nome+ ".")

# peço para o usuario inserir a idade

idade = input("Quantos anos você tem? ")

# aqui especifico que o usuario não pode ultilizar caracteres com idade.isdigit()

while not idade.isdigit():
    print("Porfavor, digite apenas números.")
    idade = input("Quantos anos você tem? ")

idade = int(idade)

# no final ele classifica e printa as opcoes selecionadas

print("Você possui, " , idade , " anos.")1