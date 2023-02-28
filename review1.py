# print("hello")
# print('2+3*4')
# print(2+3*4)
# print((2+3)*4)

# score = 0
# print("score is:", score)
# score = score + 1
# print("score is:", score)
# score += 1
# print("score is:", score)
# score = score - 1
# print("score is:", score)
# score -= 1
# print("score is:", score)


# print("he said:\"do some thing\"")
# print('he said:"do some thing"')
# print('''he said:"do some thing"''')

# print("hello.\nwelcome to our python class.")
# print("""hello.
# welcome to our python class.""")

# print("id\tname\tage")
# print("01\tsina\t10")

# print("hi.\rwelcome to our python class.")
# print("python.\rclass")
# print("hello.\rwelcome to python class.\rwelcome to pygame")

# +   -   *    /
# //
# print(3/2)
# print(3//2)

# print(4 % 2)
# print(5 % 2)
# print(2*2*2)
# print(2 ** 3)


# n1 = input('enter a number: ')
# n2 = int(input('enter a number: '))
# print(n1 * n2)
# print('*' * 5)

# برنام ای بنویسید که نام یک دانش آموز را از ورودی دریافت نماید و
# نمرات  5 درس را از ورودی بگیرد و معدل او را محاسبه نماید
# در انتها پیغامی به صورت زیر پرینت کند
# reza's average is:95

name = input("enter student's name: ")
total = 0
for i in range(5):
    score = float(input(f'enter score {i+1}: '))
    total += score  # total = total + score
print(f"{name}'s average is:{total/5}")


name = input("enter student's name: ")
scores = []
for i in range(5):
    score = float(input(f'enter score {i+1}: '))
    scores.append(score)
print(f"{name}'s average is:{sum(scores)/5}")
