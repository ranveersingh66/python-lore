#Number guessing game
import random
ran = random.randint(1, 100)
tries = 0

while True: 
  tries += 1
  user = int(input("guess a number between 1 and 100: "))
  if user == ran:
    print("You guessed it right!")
  elif user > ran:
    print("Go lower!")
  elif user < ran:
    print("Go higher!")

