import random 
name = input("what is your name?")
print(f"welcome to the game {name}")
loop = int(input("what time game? "))
lap = 1
print(f"{name},please choice a future :")
score_palyer = 0
score_sys = 0

while lap < loop:
    print("1.rock\n2.paper\n3.sicssor")
    user_input = input("?")
    choices =("rock","paper","scissor")
    sys_choice = random.choice(choices)
    print(f"system choice is {sys_choice}")

    if user_input == "rock":
        if sys_choice == "rock":
            print("Draw!")
            lap += 1
        elif sys_choice == "paper":
            print("Lose!")
            lap += 1
            score_sys += 1 
        elif sys_choice == "scissor":
            print("win")
            lap += 1
            score_palyer += 1
    elif user_input == "paper":
        if sys_choice == "paper":
                print("Draw!")
                lap += 1
        elif sys_choice == "scissor":
                print("Lose!")
                score_sys += 1 
                lap += 1 
                

        elif sys_choice == "rock":
                print("Win!")
                lap +=1
                score_palyer += 1
    elif user_input == "scissor":
        if sys_choice == "rock":
                print("Lose!")
                lap +=1
                score_sys += 1
        elif sys_choice == "paper":
                print("Win!")
                score_palyer += 1
                lap +=1
        elif sys_choice == "scissor":
                print("Draw!")
                lap +=1
    else : 
        print("Wrong!try again")

print(f"socre player : {score_palyer}")
print(f"score system :{score_sys}")