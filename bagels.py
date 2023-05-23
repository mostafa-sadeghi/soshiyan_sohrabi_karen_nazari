import random
import string
from colorama import init, Fore, Back, Style
init()
# print(Style.NORMAL + Fore.RED + Back.GREEN + "Hello EveryBody",end="")

NUM_DIGITS = 3
MAX_TIMES_To_GUESS = 10

print(f'''Welcome to Bagels Game,
you must guess a {Fore.GREEN + str(NUM_DIGITS) + Style.RESET_ALL} digits number and you have {Fore.RED + str(MAX_TIMES_To_GUESS) + Style.RESET_ALL} times to guess it.
After each guess, We show you One Hint:
{Fore.MAGENTA}"Fermi"{Style.RESET_ALL}  means     : (one digit is at the right position),
{Fore.CYAN}"Pico"{Style.RESET_ALL}   means     : (one digit is in the code but on a different position),
{Fore.LIGHTRED_EX}"Bagels"{Style.RESET_ALL} means     : (none of the digits are correct).
''')


def generate_secret_number():
    numbers = list(string.digits)
    random.shuffle(numbers)
    random_number = ''
    for i in range(NUM_DIGITS):
        random_number = random_number + numbers[i]
    return random_number


def check_user_guess(guess, secret):
    if guess == secret:
        return 'You won'
    # TODO


secret_number = generate_secret_number()
print("secret numeber generated...")
user_guess = input(f'Enter {NUM_DIGITS} digits number: ')
print("user_guess:", user_guess)

check_user_guess(user_guess, secret_number)
