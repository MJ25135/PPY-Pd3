import getpass
import random

print("Papier, Kamień, Nożyce")
print('Wybierz tryb gry: '
      '\n 1. Gracz vs Komputer'
      '\n 2. Gracz vs Gracz')
choice = input()
print("Gra odbywa sie ilosci podanych rund, gdzie każda runda odbywa się w systemie"
      "\nBo5 (Best of Five)")

rounds = input("Podaj ilość rund: \n")


def print_options():
    print("\nWybierz twój wybór:"
          "\n1. Kamień"
          "\n2. Papier"
          "\n3. Nożyce")


if int(choice) == 1:
    print("Gra przeciwko komputerowi.")
    playerRoundScore = 0
    aiRoundScore = 0
    for x in range(0, int(rounds)):
        print("\nRunda ", x+1)
        playerScore = 0
        aiScore = 0
        while playerScore != 3 and aiScore != 3:
            scores = []
            print_options()
            player = input()
            ai = random.randint(1, 3)

            if int(player) == int(ai):
                dec = ""
                if int(player) == 1:
                    dec = "Kamień"
                elif int(player) == 2:
                    dec = "Papier"
                elif int(player) == 3:
                    dec = "Nożyce"

                print("Gracz: " + dec + " - " + dec + " :Komputer")
                print("Wynik: ", playerScore, " - ", aiScore)

            elif int(player) == 1 and int(ai) == 2:
                print("Gracz: Kamień - Papier :Komputer")
                aiScore += 1
                print("Wynik: ", playerScore, " - ", aiScore)
            elif int(player) == 1 and int(ai) == 3:
                print("Gracz: Kamień - Nożyce :Komputer")
                playerScore += 1
                print("Wynik: ", playerScore, " - ", aiScore)
            elif int(player) == 2 and int(ai) == 1:
                print("Gracz: Papier - Kamien :Komputer")
                playerScore += 1
                print("Wynik: ", playerScore, " - ", aiScore)
            elif int(player) == 2 and int(ai) == 3:
                print("Gracz: Papier - Nożyce :Komputer")
                aiScore += 1
                print("Wynik: ", playerScore, " - ", aiScore)
            elif int(player) == 3 and int(ai) == 1:
                print("Gracz: Nożyce - Kamien :Komputer")
                aiScore += 1
                print("Wynik: ", playerScore, " - ", aiScore)
            elif int(player) == 3 and int(ai) == 2:
                print("Gracz: Nożyce - Papier :Komputer")
                playerScore += 1
                print("Wynik: ", playerScore, " - ", aiScore)

        if playerScore > aiScore:
            playerRoundScore += 1
        elif aiScore > playerScore:
            aiRoundScore += 1
        print("Wynik w rundach: "
              "\n Gracz: ",playerRoundScore,  " - ", aiRoundScore,  " :Komputer")

    if playerRoundScore > aiRoundScore:
        print("\nWygrywa gracz!")
    elif playerRoundScore < aiRoundScore:
        print("\nWygrywa Komputer")
    else:
        print("\nRemis")
    print("Koniec Gry")

elif int(choice) == 2:
    player1RoundScore = 0
    player2RoundScore = 0
    player1Score = 0
    player2Score = 0

    p1Name = input("Podaj Nazwe gracza 1: ")
    p2Name = input("Podaj Nazwe gracza 2: ")

    while player1Score != 3 and player2Score != 3:
        print_options()
        player1 = getpass.getpass("\nWybór " + p1Name + ": ")
        player2 = getpass.getpass("Wybór " + p2Name + ": ")

        if int(player1) == int(player2):
            dec = ""
            if int(player1) == 1:
                dec = "Kamień"
            elif int(player1) == 2:
                dec = "Papier"
            elif int(player1) == 3:
                dec = "Nożyce"

            print(p1Name + ": " + dec + " - " + dec + ": " + p2Name)
            print("Wynik: ", player1Score, " - ", player2Score)

        elif int(player1) == 1 and int(player2) == 2:
            print("Gracz: Kamień - Papier :Komputer")
            player2Score += 1
            print("Wynik: ", player1Score, " - ", player2Score)
        elif int(player1) == 1 and int(player2) == 3:
            print("Gracz: Kamień - Nożyce :Komputer")
            player1Score += 1
            print("Wynik: ", player1Score, " - ", player2Score)
        elif int(player1) == 2 and int(player2) == 1:
            print("Gracz: Papier - Kamien :Komputer")
            player1Score += 1
            print("Wynik: ", player1Score, " - ", player2Score)
        elif int(player1) == 2 and int(player2) == 3:
            print("Gracz: Papier - Nożyce :Komputer")
            player2Score += 1
            print("Wynik: ", player1Score, " - ", player2Score)
        elif int(player1) == 3 and int(player2) == 1:
            print("Gracz: Nożyce - Kamien :Komputer")
            player2Score += 1
            print("Wynik: ", player1Score, " - ", player2Score)
        elif int(player1) == 3 and int(player2) == 2:
            print("Gracz: Nożyce - Papier :Komputer")
            player1Score += 1
            print("Wynik: ", player1Score, " - ", player2Score)

    if player1Score > player2Score:
        player1RoundScore += 1
    elif player2Score > player1Score:
        player2RoundScore += 1

    if player1RoundScore > player2RoundScore:
        print("Wygrywa " + p1Name)
    elif player1RoundScore < player2RoundScore:
        print("Wygrywa " + p2Name)
    else:
        print("Remis")
    print("Koniec Gry")
