from random import randrange

secret_num = randrange(0, 5)
guess_count = 0
guess_limit = 3

print('Guess a number 1 - 5')
print('You have 3 guesses.')

while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    
    if guess == secret_num:
        print('You win!')
        break
    elif guess != secret_num:
        print('Try again.')
else: print('Better luck next time, bucko!')

