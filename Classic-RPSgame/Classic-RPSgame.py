import random

game_action=["rock","paper","scissor"]

while True:
 guess=random.choice(game_action)

 user_guess=input("enter your choice:").lower()
 print(f"Computer choosed:{guess}")

 if user_guess==guess:
  print("its a tie break")
 elif (user_guess=="rock" and guess=="scissor") or \
      (user_guess=="paper" and guess=="rock") or \
      (user_guess=="scissor" and guess=="paper"):
     print("You Won !!!")
 elif user_guess in game_action:
  print("You Lose!!!")
 else:
  print("invalid input.")

 play_again = input("\nWanna continue? (yes/no): ").lower() 
 if play_again == "no": 
    print("Thanks for playing! Goodbye :)")
    break
 