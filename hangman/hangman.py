from random import choice
import sys

print("HANGMAN""\nThe game will be available soon.")
print("If you want start game press ",1,"")
print("If you want to finish the game press ",0,"")

user_input = int(input(">"))
if user_input == 0:
    sys.exit("Goodbye")


wrong_max = 7
words = ('python', 'java', 'javascript', 'php')
player_word = choice(words)
far = '-' * len(player_word)
wrong = 0
used_words = []

while wrong < wrong_max and far != player_word and user_input == 1:

    print("\n You used this letter >\n", used_words)
    print("\n At the moment the word looks like this >\n", far)

    guess = input("\n Please enter above guess > ")

    if len(guess) > 1:
        sys.exit("You must enter one letter.Try again!")
    elif guess == "0":
        sys.exit("Goodbye")
    elif guess == guess.upper():
        sys.exit("Turn capslock off or don't use numbers and start again!")

    while guess in used_words:
        print("You already guessed that letter!", guess)
        guess = input("Please enter your guess >")

    used_words.append(guess)

    if guess in player_word:
        print("Great! '" + guess + "the word")

        new = ''
        for x in range(len(player_word)):
            if guess == player_word[x]:
                new += guess
            else:
                new += far[x]
        far = new
    else:
        print("\n Sorry, no letter " + guess + " in the word")
        wrong += 1

if wrong == wrong_max:
    print("\nYou lost!")

else:
    print("\nYou survived!")

print("The hidden word was " + player_word + " ")
