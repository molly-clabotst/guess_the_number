import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'


def configure_range():
    '''Set the high and low values for the random number'''
    return 1, 10


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    # Learned how to do this from this source
    # https://www.techbeamers.com/use-try-except-python/
    try:
        '''get user's guess'''
        return int(input('Guess the secret number? '))
    except Exception as ex:
        print(ex)


def check_guess(guess, secret):
    try:
        '''compare guess and secret, return string describing result of comparison'''
        if guess == secret:
            return correct
        if guess < secret:
            return too_low
        if guess > secret:
            return too_high
    except Exception as ex:
        print(ex)



def main():
    (low, high) = configure_range()
    secret = generate_secret(low, high)

    attempts = 0
    while True:
        guess = get_guess()
        result = check_guess(guess, secret)
        attempts += 1
        print(result)

        if result == correct:
            break

    print("You succeeded in " +
          str(attempts) + " wrong attempts!")


if __name__ == '__main__':
    main()
