playAgain = "yes"
rock = "rock"
paper = "paper"
scissors = "scissors"
winp1 = "Player 1 wins! Congratulations!"
winp2 = "Player 2 wins! Congratulations!"

while playAgain == "yes":
    p1 = input("Player 1, Rock-Paper-Scissors shoot!: ") # player1 move
    p2 = input("Player 2, Rock-Paper-Scissors shoot!: ") # player2 move
    p1 = p1.lower()
    p2 = p2.lower()

    if p1 == p2:
        print("Draw!")
    elif p1 == rock and p2 == scissors:
        print(winp1)
    elif p1 == scissors and p2 == paper:
        print(winp1)
    elif p1 == paper and p2 == rock:
        print(winp1)
    else:
        print(winp2)

    playAgain = input("\nIf you would like to play again, enter \'yes\'.\nTo exit, enter any other key:")