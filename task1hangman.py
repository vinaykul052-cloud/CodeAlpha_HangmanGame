import random

# Word list
words = ["python", "hangman", "developer", "program", "code"]

# Randomly select word
word = random.choice(words)

# Game setup
guessed_word = ["_"] * len(word)
attempts = 6
guessed_letters = []

print("🎮 Welcome to Hangman Game!")
print("Guess the word letter by letter.\n")

# Game loop
while attempts > 0 and "_" in guessed_word:
    print("\nCurrent word:", " ".join(guessed_word))
    print("Attempts left:", attempts)
    print("Guessed letters:", " ".join(guessed_letters))

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single valid letter!")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("❌ Wrong guess!")
        attempts -= 1

# Game result
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)