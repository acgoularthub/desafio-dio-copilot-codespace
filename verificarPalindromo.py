# testar se uma palavra é um palíndromo

def palindromo(palavra):
    return palavra == palavra[::-1]

palavra = input("Digite uma palavra: ")
if palindromo(palavra):
    print("É um palíndromo")
else:
    print("Não é um palíndromo")

    