import random


words = [
    "apple", "banana", "grape", "orange", "cherry",
    "peach", "mango", "papaya", "lemon", "melon",
    "carrot", "tomato", "potato", "onion", "garlic",
    "pepper", "cucumber", "spinach", "broccoli", "pumpkin"
]


words = [w for w in words if 4 <= len(w) <= 8]

word = random.choice(words)
word_letters = list(word)

display = ['_'] * len(word)

attempts = 6
guessed_letters = []

print("🎮 Let's play Hangman!")
print("Word to guess:", ' '.join(display))


while attempts > 0 and '_' in display:
    guess = input("Guess a letter: ").lower()

    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_letters:
        for i, letter in enumerate(word_letters):
            if letter == guess:
                display[i] = guess
        print("✅ Good guess!")
    else:
        attempts -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts}")

    print(' '.join(display))


if '_' not in display:
    print("🎉 Congratulations! You guessed the word:", word)
else:
    print("💀 Game Over! The word was:", word)