import random
import time

print("Welcome to hangman")


def get_num_attempts():
    while True:
        num_attempts = input("How many attempts would you like? [1-25]: ")
        try:
            num_attempts = int(num_attempts)
            if 0 < num_attempts <= 25:
                return num_attempts
            else:
                print("{0} is not in the range 1-25".format(num_attempts))

        except ValueError:
            print('{0} is not an integer between 1 and 25'.format(num_attempts))


def get_word():
    filename = "3000.txt"
    with open(filename) as f:
        words = f.readlines()
    return random.choice(words)


def play(word):
    success_attempts = 0
    word_completion = "_" * len(word)
    guessed = False
    guesses_letters = []
    attempts = get_num_attempts()
    total_attempts = attempts
    print("Word to guess: " + word_completion)
    print("Attempts remaining: " + str(attempts))
    start = time.time()
    while not guessed and attempts > 0:
        guess = input("\nEnter a letter: ")
        if guess in guesses_letters:
            print("You have already guessed ", guess)
        elif guess not in word:
            print(guess, "is not in the word.")
            attempts -= 1
            guesses_letters.append(guess)
        else:
            # print("Good work {0} is in the word".format(guess))
            success_attempts += 1
            guesses_letters.append(guess)
            word_as_list = list(word_completion)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                word_as_list[index] = guess
            word_completion = "".join(word_as_list)
            if "_" not in word_completion:
                guessed = True
        print("Word to guess: {0}".format(word_completion))
        print("Attempts remaining: {0}".format(attempts))
    if guessed:
        print("\n")
        print("Congratulations, You guessed right")
        end = time.time()
        print("You did it in " + str(total_attempts - attempts + success_attempts) + " attempts")
        print("Time taken: {0} seconds".format((end - start)))
    else:
        print("Hard Luck. The word was: {0}".format(word))


def main():
    print("Starting...")
    # word = get_word()
    word = "hello"
    play(word)


if __name__ == "__main__":
    main()
