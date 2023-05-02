import random

NUM_DIGITS = 3
MAX_GUESSES = 10

print(f'''Welcome to Bagels Game,
you must guess a {NUM_DIGITS} digits number and you have {MAX_GUESSES} times to guess it.
After each guess, We show you One Hint: 
"Fermi"  means     : (one digit is at the right position), 
"pico"   means     : (one digit is in the code but on a different position), 
"bagels" means     : (none of the digits are correct).
''')


#exercise : 
'''
تابعی برای تولید اعداد سه رقمی تصادقی با رقم های غیرتکراری

'''
def generate_secret_number():
    pass




def getClues(guess, secret_number):
    pass
'''
تابعی برای نمایش وضعیت حدس کاربر


مثال فرض کنید عددی که کاربر باید حدس می زده 
325

اگر بازیکن 
325 
را وارد کند 
برنده میشه


اگر 

134
برنامه عیارت زیر را نمایش می دهد
['pico']

اگر حدس کاربر
315 باشد
['fermi', 'fermi']


اگر حدس کاربر 
351
['fermi','pico']


اگر حدس کاربر 769
bagels
'''


secret_number = generate_secret_number()
number_guesses = 1
while number_guesses < MAX_GUESSES:
    # گرفتن حدس کاربر   guess

    clues = getClues(guess, secret_number)















# string = 'me and amir and sara are firends.'
# print(string.count('and'))
# print(string.split().count("and"))
# word = ''
# all_words = []
# for c in string:
#     word += c
#     if c == ' ' or c == '.':
#         all_words.append(word[:-1])
#         word = ''
# print(all_words)