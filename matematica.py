# solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

operacao = input("Digite a operação que deseja realizar: \n 1- Soma \n 2- Subtração \n 3- Multiplicação \n 4- Divisão \n")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if operacao == "1":
    print("O resultado da soma é: ", soma(num1, num2))
elif operacao == "2":
    print("O resultado da subtração é: ", subtracao(num1, num2))
elif operacao == "3":
    print("O resultado da multiplicação é: ", multiplicacao(num1, num2))
elif operacao == "4":
    print("O resultado da divisão é: ", divisao(num1, num2))
else:
    print("Operação inválida")
