# solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

palavra = input("Digite uma palavra: ")
numero = int(input("Digite o numero de vezes que deseja repetir a palavra: "))
             
#a palavra é repetida o número de vezes informado mas deve pular uma linha para cada repetição

print((palavra + "\n") * numero)