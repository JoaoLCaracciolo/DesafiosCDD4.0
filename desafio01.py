#Faça um código para ler 5 nomes de usuários e suas respectivas senhas, e armazenar cada lista em um array diferente, após completar a digitação, imprimir , nome, senha e posição dos dados no array.Altere o sistema anterior e faça um sistema de login, pedind a senha do usuário e mostrando seu nome e a mensagem, login efetuado com sucesso
nomes = [0, 0, 0, 0, 0]
senha = [0, 0, 0, 0, 0]
i = 0
x = 0
for i in range(2):
    print(f"=========== {i+1}°CADASTRO=============")
    nomes[i] = input("Nome:")
    senha[i] = input("Senha:")
    print("===================================\n")
tentativa = 0
print("---------------LOGIN---------------")
while tentativa != 3:
    verificarNome = input("Nome:")
    for x in range(2):
        if nomes[x] == verificarNome:
            tentativa = 0
            while tentativa != 3:
            #for m in range(3):
                verificarSenha = input("Senha:")
                if senha[x] == verificarSenha:
                    print("----LOGIN EFETUADO COM SUCESSO-----")
                    print(f"Posição:{x}\nNome:{nomes[x]}\nSenha:{senha[x]}")
                    print("-----------------------------------")
                    tentativa = 3
                    break
                else:
                    print("\nXXXXXX Senha invalida XXXXXX\n")
                    tentativa += 1
    if tentativa != 3:
        print("\nXXXXXX Usuario Invalido XXXXXX\n")
        tentativa += 1
