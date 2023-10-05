"""Faça um algoritmo que leia 30 valores do
tipo inteiro e armazene-os em um vetor.
A seguir, o algoritmo deverá informar
(1) todos os números pares que existem no
vetor;
(2) o menor e o maior valor existente no
vetor;
(3) quantos dos valores do vetor são
maiores que a média desses valores:"""
numeros = [0]*30
contador = 0
maiorNum = 0
soma = 0

for i in range(30):
    numeros[i] = int(input(f"Digite o {i+1}° numero:"))
    soma += numeros[i]

media = soma/30
menorNum = numeros[0]

print("-----Numeros Pares-----")
for o in range(30):
    if numeros[o] % 2 == 0:
        print(numeros[o], end="-")

for p in range(30):
    if numeros[p] > maiorNum:
        maiorNum = numeros[p]
    if numeros[p] < menorNum:
        menorNum = numeros[p]

for k in range(30):
    if numeros[k] > media:
        contador += 1

print(f"\nMaior numero:{maiorNum}\nMenor Numero:{menorNum}\nNumeros Maiores que a media:{contador}")
