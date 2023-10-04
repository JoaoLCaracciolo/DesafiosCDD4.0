"""Faça um código para ler um valor N qualquer (que
será o tamanho dos vetores). Após, ler dois
vetores A e B (de tamanho N cada um) e depois
armazenar em um terceiro vetor Soma a soma dos
elementos do vetor A com os do vetor B
(respeitando as mesmas posições) e escrever o
vetor Soma"""
i = 0

nVet = int(input("Digite a quantidade de vetores:"))
vet1 = [0]*nVet
vet2 = [0]*nVet
vetSoma = [0]*nVet

for i in range(nVet):
    vet1[i] = int(input(f"Digite o {i+1}° valor do vetor 1:"))
    vet2[i] = int(input(f"Digite o {i+1}° valor do vetor 2:"))
    vetSoma[i] = vet1[i] + vet2[i]

print(f"Vetor A:{vet1}\nVetor B:{vet2}\nVetor Soma:{vetSoma}")
