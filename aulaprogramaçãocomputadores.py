nota_1 = float(input("Digite sua nota: "))
nota_2 = float(input("Digite sua nota: "))
nota_3 = float(input("Digite sua nota: "))
media = (nota_3 + nota_2 + nota_1) / 3

if (media >= 5):
    print("Parabéns você foi aprovado")
else:
    print("Infeliz você foi reprovado, tente novamente!")

senha = ("123456")
senha_2 = input("Digite sua senha: ")

if (senha_2 == senha):
    print("acesso liberado")
else:
    print("acesso negado")

a = int(input("Digite um número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
soma = (a + b)

if (soma < c):
    print("A soma é menor")
else:
    print("a soma é maior ou igual")

salario = float(input("Digite seu salário: "))


if (salario <= 300,00):
    print("seu salário é: ", salario + (salario * 0.35))
else:
    print("seu salário é: ", salario + (salario * 0.15))
