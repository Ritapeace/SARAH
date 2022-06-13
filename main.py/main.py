import random
Game = True
while Game:

    GameList = ["R", "P", "S"]
    
    print ("Select an option from: ", GameList)
    Player = input ("Enter your option: ")
    rlist = random.choice(GameList)
    print (rlist)
    if Player == rlist:
        print(f"Both players selected {Player}. It's a tie!")
    elif Player == "R":
        if rlist == "S":
            print("Rock beats scissors! You win!")
            print("The computer lose")
        else:
            print("Paper beats rock! You lose.")
            print("The Computer wins")
    elif Player == "P":
        if rlist == "R":
            print("Paper beats rock! You win!")
            print("The computer lose")
        else:
            print("Scissors beats paper! You lose.")
            print("The computer wins")
    elif Player == "S":
        if rlist == "P":
            print("Scissors beats paper! You win!")
            print("The computer lose")
        else:
            print("Rock beats scissors! You lose.")
            print("The computer wins")
    elif Player != "S" or "P" or "R":
        if rlist != "S" or "P" or "R":
            print("Invalid entry")


            playagain=str(input("Do you want to play again, yes or no? "))
            if playagain == "no":
                Game = False
                break
                   

        
