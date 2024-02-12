#Number Guessing Game Objectives:

# Include an ASCII art logo.
import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
number=random.randint(1,100)
def set_difficulty():  
  difficulty=input("Choose a difficulty. Type 'easy' or 'hard':") 
  if(difficulty=="easy"):
    turns=10
    print("You have 10 attempts remaining to guess the number.")
  else:
    turns=5
    print("You have 5 attempts remaining to guess the number.")
  return turns


def check_answer(guess,answer):
  if(guess==answer):
    print(f"You got it! The answer was {number}.")
    return True
  elif answer<guess:
    print("Too high.\nGuess again.")
    return False
  else:
    print("Too low. \nGuess again.")
    return False
    
is_game_over=False
attempts=set_difficulty()
while attempts!=0 and not is_game_over:
  user_number=int(input("Make a guess: "))
  is_game_over=check_answer(user_number,number)
  attempts-=1
  if(attempts>0 and is_game_over==False):
      print(f"You have {attempts} attempts remaining to guess the number.")
 


  