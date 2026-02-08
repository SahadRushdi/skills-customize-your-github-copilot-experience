
# 📘 Assignment: Games in Python

## 🎯 Objective

Build a classic Hangman word-guessing game to practice Python string manipulation, loops, conditionals, and user input handling while creating an interactive gaming experience.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Create the foundation of the Hangman game by setting up a word list and implementing random word selection to start each game.

#### Requirements
Completed program should:

- Define a list of at least 5-10 words for the game
- Use the `random` module to randomly select a word from the list
- Initialize game variables (attempts remaining, guessed letters, current progress)
- Set a reasonable number of incorrect guesses allowed (e.g., 6-8 attempts)

### 🛠️ Game Logic and User Interaction

#### Description
Implement the core game loop that accepts player input, validates guesses, and updates the game state accordingly.

#### Requirements
Completed program should:

- Accept single letter guesses from the player using `input()`
- Validate that the input is a single letter and hasn't been guessed before
- Display the current progress in `_ _ _` format showing correctly guessed letters
- Track and display incorrect guesses remaining
- Update the word progress when correct letters are guessed
- Example display:
  ```
  Word: _ a _ _ _ a _
  Guesses remaining: 5
  Enter a letter: 
  ```

### 🛠️ Win/Lose Conditions

#### Description
Implement the game ending logic to determine when the player wins or loses, and display appropriate messages.

#### Requirements
Completed program should:

- Check if the word is completely guessed (player wins)
- Check if attempts are exhausted (player loses)
- Display a congratulatory message when the player wins
- Reveal the correct word and display a game over message when the player loses
- End the game loop when either condition is met
