import random
while True:
    computer_choice = random.randint(1,3)
    a=input("Enter your choice: rock/paper/scissors:").lower()
    if computer_choice == 1:
        computer_choice = "rock"
    elif computer_choice == 2:
        computer_choice = "paper"
    elif computer_choice == 3:
        computer_choice = "scissors"
    print(f"Computer choice is {computer_choice}")    
    if a == computer_choice:
            print("Draw!")
    elif a == "rock" and computer_choice == "scissors":
            print("You win!")
    elif a == "paper" and computer_choice == "scissors":
            print("Computer Wins")
    elif a == "scissors" and computer_choice == "rock":
            print("Computer Wins")
    elif a == "scissors" and computer_choice == "paper":
            print("YOU Win")
    elif a == "rock" and computer_choice == "paper":
            print("YOU Win")
    elif a == "paper" and computer_choice == "rock":
            print("YOU Win")
    b = input("Do You Wanna Continue The Game YES/NO: ").lower()
    

    if b == "yes":
        print("Repeating Game")
    else:
        break
        

