"""Escreva um algoritmo que solicite ao
usuário a entrada de 5 nomes, e que exiba
a lista desses nomes na tela.
Após exibir essa lista, o programa deve
mostrar também os nomes na ordem
inversa em que o usuário os digitou, um
por linha."""

listaNomes = [0, 0, 0, 0, 0]
i = 0

for i in range(5):
    listaNomes[i] = input(f"Digite o {i+1}° Nome:")

print("----------LISTA----------")
for x in range(5):
    print(f"{x+1}°Nome:{listaNomes[x]}")

print("------LISTA INVERSA------")
for i in range(i, -1, -1):
    print(f"{i + 1}°Nome:{listaNomes[i]}")
