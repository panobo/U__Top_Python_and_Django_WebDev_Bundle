# FIZZBUZZ game
# if number is divisible by 3 -> print fizz
# if number is divisible by 5 -> print buzz
# if number is divisible by 3 and 5 -> print fizzbuzz
# for every other number just print out the number

from os import system

system('clear')


number = 1
while (number <= 100):
    if (number % 3 == 0) and (number % 5 == 0):
        print(f'{number} - FIZZBUZZ')
    elif number % 3 == 0:
        print(f'{number} - FIZZ')
    elif number % 5 == 0:
        print(f'{number} - BUZZ')
    else:
        print(number)
    
    number += 1
