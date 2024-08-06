"""Imagine que você está trabalhando na Organo, uma plataforma de organogramas para empresas. Você foi designado para criar um simples script em Python que coleta o nome de um departamento e o nome da pessoa responsável por ele, para depois imprimir uma mensagem personalizada.

Qual trecho de código em Python abaixo irá corretamente coletar as informações e imprimir a mensagem desejada, seguindo o formato: "O departamento de [Departamento] é liderado por [Responsável]."?"""
departamento = input("Digite o nome do departamento: ")
responsavel = input("Digite o nome do responsável: ")
print("O departamento de " + departamento + " é liderado por " + responsavel + ".")
print(f'O departamento de {departamento.upper()} é liderado por {responsavel.upper()}')