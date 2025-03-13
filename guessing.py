

import random

def number_guessing():
  print("Well come to number guessing game.")
  print("I'm thinking of number between 1 and 20, what is it ? ")
  number_to_guess = random.randint(1, 20)  

  attempts = 0
    
  while True:
     try:
        guess = int(input("Enter Your Guess Number: "))
        if guess > 20:
            print("Oops!!!, I'm thinking of number between 1 and 20, what is it ?")

        attempts += 1
        if attempts == 6:

            print("sorry, you reached maximum attempts")
            break

        if guess < number_to_guess:
            print("Too low, Try again!")
        elif guess > number_to_guess:
            print("Too high, Try again")    
        else:
            print(f"Congradulations!, you guessed the number {number_to_guess}, in {attempts} attempts")  

            break
            
     except ValueError:
        print("please enter a valid number ")          



number_guessing()



"""
concepts that the project deals with
- function
- looop(while loop)
- exception handling
- input()
- formated string
- if else 
"""
