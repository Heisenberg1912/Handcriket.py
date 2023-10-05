import random

def play_hand_cricket():
    print("Welcome to Hand Cricket!")
    
    
    user_choice = input("Enter 'bat' to bat or 'ball' to bowl: ").lower()
    
    if user_choice not in ['bat', 'ball']:
        print("Invalid choice. Please enter 'bat' or 'ball'.")
        return
    
    computer_choice = 'bat' if user_choice == 'ball' else 'ball'
    
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    total_runs = 0
    
    while True:
        user_runs = int(input("Enter runs (1 to 6): "))
        
        if user_runs < 1 or user_runs > 6:
            print("Invalid runs. Please enter a number between 1 and 6.")
            continue
        
        computer_runs = random.randint(1, 6)
        print(f"Computer played: {computer_runs}")
        
        if user_runs == computer_runs:
            print("Out! Your inning ends.")
            break
        
        total_runs += user_runs
    
    print(f"You scored {total_runs} runs.")
    
    if user_choice == 'bat':
        print("You need to defend this score!")
    else:
        print("Now it's your turn to chase!")


play_hand_cricket()
