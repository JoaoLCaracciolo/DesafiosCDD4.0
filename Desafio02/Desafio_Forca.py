import random

from biblioteca_Forca import boneco

# 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'

# palavras que serão utilizadas na forca
palavrasForca = ["python", "ruby", "java", "kotlin"]

# escolher aleatoriamente uma palavra dentre as palavraForca
palavraEscolhida = random.choice(palavrasForca)

#variavel das letras que foram acertadas
letrasCorretas = []

#Letras que já foram utilizadas
letrasUtilizadas = []

print("--------------------Bem-Vindo ao Jogo Da Forca--------------------")
print("Você terá 6 tentativas para adivinhar a palavra")
print("------------------------------------------------------------------\n")
#Montar array para "_"
for x in palavraEscolhida:
    letrasCorretas += '_'

#contador das tentativas da forca
tentativas = 0

while tentativas != 6:

    print(boneco(tentativas))
    #Transformar array para string
    print(" ".join(letrasCorretas))
    print(f"\nVocê tem {6 - tentativas} tentativas")

    #receber variavel do usuario
    letraUser = input("Digite uma letra:").lower()

    #testar se existe mais de 1 letra
    if len(letraUser) > 1:
        print("\nDigite uma letra por vez")
        continue

    #testar se a letra já foi utilizada
    if letraUser in letrasUtilizadas:
        print(f"Você já utilizou a(s) letra(s): {'-'.join(letrasUtilizadas).upper()}")
        continue

    #testar se é uma letra
    if letraUser not in "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz":
        print("\nDigite apenas letras")
        continue

    else:
        letrasUtilizadas += letraUser

    #Passar as letras que foram corretas para a palavra secreta
    if letraUser in palavraEscolhida:
        for i in range(len(palavraEscolhida)):
            if letraUser == palavraEscolhida[i]:
                letrasCorretas[i] = palavraEscolhida[i]
    else:
        tentativas += 1
    #verificar se ainda existe _ em letras corretas para fizenliar a forca avisando que o usuario ganhou
    if "_" not in letrasCorretas:
        print(f"\nParabéns! Você acertou!!😎\nA palvra era {palavraEscolhida}")
        tentativas = 6

if tentativas == 6 and "_" in letrasCorretas:
    print(boneco(tentativas))
    print("\nVocê Perdeu!!!😭")
