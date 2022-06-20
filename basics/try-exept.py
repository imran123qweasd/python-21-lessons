import random
guesses_made = 0
name = input('Привет! Как тебя зовут?\n')

# рандом от 1-100
number = random.randint(1, 100)
print ('шикарно, {0}, я загадал число между 1 и 100. Сможешь угадать?'.format(name))

# число попыточек 10
while guesses_made < 10:
    
    # он угадывает
    guess = int(input('Введи число: '))
    
    # + попытка
    guesses_made += 1

    if guess < number:
        print ('бери больше.')

    if guess > number:
        print ('бери меньше.')

    if guess == number:
        break

if guess == number:
    print ('ептить, {0}! Ты угадал мое число, за {1} попыток!'.format(name, guesses_made))
else:
    print (' ха-ха лох , я загадал {0}'.format(number))
        
