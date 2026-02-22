Number Guessing Game 🎯

A simple beginner-level Python project where the user tries to guess a randomly generated number between 1 and 20.

📌 Project Description

This is a command-line game written in Python.
The program generates a random number between 1 and 20, and the player has 6 attempts to guess it correctly.

The program provides feedback after each guess:

If the guess is too low → “Too low, Try again!”

If the guess is too high → “Too high, Try again!”

If the guess is correct → Congratulations message with number of attempts

If maximum attempts are reached → Game ends

It also handles invalid inputs (e.g., letters instead of numbers).

🚀 Features

Random number generation

Maximum 6 attempts limit

Input validation using exception handling

Clear feedback messages

Beginner-friendly logic

🧠 Concepts Covered
   This project demonstrates the following Python concepts:
   Functions
   While loop
   Conditional statements (if, elif, else)
   Exception handling (try, except)
    User input (input())
    Type casting (int())
    Formatted strings (f-strings)
    Random module (random.randint())
    🛠️ Requirements
    Python 3.x installed
    Check Python version:
    python --version
▶️ How to Run
      Save the file as:
      number_guessing.py
      Open terminal or command prompt.
      Navigate to the project folder.
      Run the program:
      python number_guessing.py
      🎮 How to Play
      The program selects a random number between 1 and 20.
      Enter your guess when prompted.
      You have 6 attempts.
      Try to guess correctly before attempts run out.

📂 Project Structure
      number_guessing.py
      README.md
      📖 Example Output
      Welcome to number guessing game.
      I'm thinking of number between 1 and 20, what is it ?
      Enter Your Guess Number: 10
      Too low, Try again!
      Enter Your Guess Number: 15
      Too high, Try again
      Enter Your Guess Number: 13
      Congratulations!, you guessed the number 13, in 3 attempts
📈 Possible Improvements
          Add difficulty levels (easy, medium, hard)
          Allow replay option
          Add score tracking
          Improve input range validation
          Convert to GUI version using Tkinter
