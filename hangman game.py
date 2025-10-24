import random

stages=["""
    +---+
    |   |
    0   |
   /|\  |
   / \  |
        |
----------
----------
""","""
    +---+
    |   |
    0   |
   /|\  |
   /    |
        |
----------
----------
""","""
    +---+
    |   |
    0   |
   /|\  |
        |
        |
----------
----------
""","""
    +---+
    |   |
    0   |
   /|   |
        |
        |
----------
----------
""","""
    +---+
    |   |
    0   |
    |   |
        |
        |
----------
----------
""","""
    +---+
    |   |
    0   |
        |
        |
        |
----------
----------
""","""
    +---+
    |   |
        |
        |
        |
        |
----------
----------
"""]


words = ["love", "hangman", "nanjing", "hakimi", "usa", "pizza", "french", "summer"]
random_word = random.choice(words)

print(random_word)

display = ["_"] * len(random_word)

print(" ".join(display))
print(stages[-1])

lives = 6
guessed = []

while "_" in display and lives > 0:

    guess_letter = input("please enter a letter: ").lower()
    if guess_letter in guessed:
        print("you have already try it")
        print(f"you have {lives} tries more")
        continue

    for position in range(len(random_word)):
        if random_word[position] == guess_letter:
            display[position] = guess_letter
    
    if guess_letter not in random_word:
        guessed.append(guess_letter)
        lives -= 1
        print(f"you have {lives} tries more")
        print(stages[lives])

    print(" ".join(display))

if "_" not in display:
    print("you win")
else:

    print("you lose")
    print("""
             +---+
             |   |
             0   |
            /|\  |
            / \  |
                 |
        ----------
        ----------
    """)