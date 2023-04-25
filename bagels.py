import random

NUM_DIGITS = 3
MAX_GUESSES = 10

# print(f'''Welcome to Bagels Game,
# you must guess a {NUM_DIGITS} digits number and you have {MAX_GUESSES} times to guess it.
# After each guess, We show you One Hint: 
# "Fermi"  means     : (one digit is at the right position), 
# "pico"   means     : (one digit is in the code but on a different position), 
# "bagels" means     : (none of the digits are correct).
# ''')
# exrcise 1 : تولید عدد تصادفی سه رقمی که رقم های آن غیر تکراری باشند.
def getSecretNum():
    number = random.randrange(100,1000)
    return number

print(getSecretNum())