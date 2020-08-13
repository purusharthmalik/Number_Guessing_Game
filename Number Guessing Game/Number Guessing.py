import random


def game():
    print("\nHello, welcome to the number-guessing game!!!")
    print("\nHow to play:")
    print("\tA random number between 1 and 100 will be chosen and you have to guess it in minimum number of guesses.\n\tYou start with a score of 100 and 10 points will be deducted for each wrong guess.")
    print("\tYou get 10 guesses")
    print("\tHappy Guessing!")

    n = random.randint(1, 101)
    score = 100
    i = 1
    guess = input("\n\nEnter your first guess:")
    if check(guess, n) == 1:
        while score != 0:
            print("Wrong guess!")
            if prime(n) == 0:
                if n > 50:
                    print('''*Hint -> The "number" is a prime number greater than 50.''')
                else:
                    print('''*Hint -> The "number" is a prime number less than 50.''')

            else:
                mul = multiple(n)
                print("*Hint -> {} is a multiple of the number.".format(random.choice(mul)))
            guess = input("Please guess again:")
            i += 1
            result = check(guess, n)
            if result == 0:
                print("\nCongratulations! You've guessed the number correctly in {} attempts.\n\t\t Correct Number = {}\n\t\t Your Score = {}".format(i, n, score))
                break
            else:
                score -= 10

    else:
        print("\nCongratulations! You guessed the correct number in your first guess!!!\n\t\t Correct Number = {}\n\t\t Your Score = {}".format(n, score))

    if score == 0:
        print("You've failed in too many attempts. Sorry!\n\t\t Correct Number = {}".format(n))


def check(guess, n):
    if int(guess) == n:
        return 0
    else:
        return 1


def multiple(n):
    m = 6
    return list(range(int(n*2), (m + 1) * int(n), int(n)))


def prime(n):
    exit = 0
    if int(n) >= 2:
        for i in range(2, int(int(n)/2)):
            if int(int(n)) % i == 0:
                exit = 1
                return 1
        if exit == 0:
            return 0


if __name__ == "__main__":
    game()
