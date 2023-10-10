jogador1 = input("Jogaodr 1\nEscolha pedra, papel ou tesoura: ")
jogador2 = input("Jogador 2\nEscolha pedra, papel ou tesoura: ")

if (jogador1 == "pedra" and jogador2 == "tesoura") or (jogador1 == "tesoura" and jogador2 == "papel") or (jogador1 == "papel" and jogador2 == "pedra"):
    print(f"Jogdor1 {jogador1}\nJogador2 {jogador2}\nJogador 1 venceu")

elif jogador1 == jogador2:
    print("Empate")

else:
    print(f"Jogdor1 {jogador1}\nJogador2 {jogador2}\nJogador 2 venceu")
