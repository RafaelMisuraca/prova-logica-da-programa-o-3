numero_sorteado = 9
max_tentativas = 3
tentativas = 0
while tentativas < max_tentativas:
    palpite = int(input("Adivinhe um número entre 1 e 10: "))
    tentativas += 1
    if palpite == numero_sorteado:
        print("Parabéns, você acertou o número sorteado.")
        break
else:
    print("Foi uma boa tentativa mas infelizmente você não conseguiu acertar o número, quem sabe na próxima vez. O número sorteado era 9")
