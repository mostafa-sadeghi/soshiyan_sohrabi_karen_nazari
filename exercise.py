# exercise 1:
#   از شما خواسته شده تا برای یک باشگاه والیبال برنامه ای بنویسید
#   که در صورت غیر مجاز بودن داوطلب پیغام مناسبی پرینت شود.
#   شرایط مجاز داوطلب برای ثبت نام در باشگاه به صورت زیر می باشد:
#   سن داوطلب نباید کمتر از 10 سال باشد
#   قد داوطلب نباید کوچکتر از 140 باشد
#   در صورتی که سن داوطلب کمتر از ده باشد پیغام مناسبی نمایش دهد و دیگر قد داوطلب را نپرسد

# message = ".... you can't register in our team, beacaues ..."

# def check_member(name, age):
#     if age < 10:
#         return f"{name}, you can't register in our team, beacause your age is lower than 10."
#     else:
#         h = float(input('enter your height: '))
#         if h < 140:
#             return f"{name}, your height is lower than 140."


# n = input('enter your name: ')
# a = int(input('enter your age: '))

# message = check_member(n, a)
# print(message)

###################################################
# exercise 2:
# for + while loop:
'''
*
* *
* * *
* * * *
* * * * * 
* * * * * *
'''
# exercise 3:
'''
* * * * * *
* * * * *
* * * * 
* * *
* *
*
'''


number = int(input('> '))

while number != 0:
    print(number % 10)
    number = number // 10  # number //= 10
