idade = int(input('Digite a sua idade: '))
if 0 <= idade <= 12:
    print("Criança.")
elif 13<=idade<18:
    print("Adolescente.")
elif idade < 0:
    print("erro, não existe idade negativa.")
else:
    print("Adulto.")