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
    help_fo_user = []
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            help_fo_user.append('Fermi')
        elif guess[i] in secret:
            help_fo_user.append('Pico')

    if len(help_fo_user) == 0:
        return 'Bagels'
    return help_fo_user


while True:
    status = ""
    secret_number = generate_secret_number()
    print("secret numeber generated...")
    # print("secret_number", secret_number)
    for i in range(MAX_TIMES_To_GUESS):
        user_guess = input(f'Enter {NUM_DIGITS} digits number: ')
        print("user_guess:", user_guess)
        help_user = check_user_guess(user_guess, secret_number)
        print(help_user)
        if user_guess == secret_number:
            status = "win"
            break
    if status == "":
        print("you lose")
    print("Do you want to continue? (y or n)")
    if input('> ') == "n":
        break
