print("*****************************************")
print("Bem vindo ao jogo de adivinhação!!!!!!!!!")
print("*****************************************")
numero_secreto = 81
total_tentativas = 3


for  tentativas in range(1,total_tentativas+1):
    print("Tentativa {} de {} ".format(tentativas,total_tentativas))
    chute = input("Digite o seu numero entre 1 e 100: ")
    numero = int(chute)

    print("Você digitou :", chute)
    numerosc = int(numero_secreto)
    acertou = numerosc == numero
    maior = numerosc > numero
    if (numero < 1 or numero > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    if (acertou):
        print("você acertou")
        break
    else:
        if (maior):
            print("O numero secreto é maior")
        else:
            print("O numero secreto é menor")
        print("Você errou")


print("Fim do jogo!")