"""Faça um código para ler um vetor de 30
números. Após isto, ler mais um número
qualquer, calcular e escrever quantas
vezes esse número aparece no vetor."""

vetorX = [0]*30
contador = 0

for i in range(30):
    vetorX[i] = int(input(f"Digite o {i+1}° numero:"))

numero = int(input("Digite um numero qualquer:"))

for x in range(30):
    if vetorX[x] == numero:
        contador += 1

print(f"O {numero} aparece {contador} vezes")
