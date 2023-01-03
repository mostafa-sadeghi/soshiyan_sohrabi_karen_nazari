'enter student name'
'enter python score'
'enter app inventor score'
'enter scratch score'
"ali's average is : 19.5"


# Exercise:
'''
برنامه ای بنویسی که 5 عدد از ورودی بگیرد و بزرگترین عدد را نمایش دهد



'''

# number1 = int(input('enter first number: '))
# number2 = int(input('enter first number: '))
# number3 = int(input('enter first number: '))

# max_number = number1
# if number2 > max_number:
#     max_number = number2

# if number3 > max_number:
#     max_number = number3

# print("max number is :", max_number)

max_number = 0
for i in range(5):
    number = int(input('enter a number'))
    if number > max_number:
        max_number = number
print("max number is: ", max_number)