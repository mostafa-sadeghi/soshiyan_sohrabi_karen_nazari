# n = 5

# for i in range(1, 6):
#     print('*' * i)


# for i in range(5,-1,-1):
#     print('*' * i)

# print('matin '*10)

# for i in range(1,10,2):
#     print(i)


for i in range(1000, 10001, 2):
    print(i)
even_numbers = []
for i in range(1000, 10001):
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)
print(len(even_numbers))

# روش بعدی بدون کمک تابع len

numbers = []
count = 0
for i in range(1000, 10001):
    if i % 2 == 0:
        count = count + 1
        numbers.append(i)
print(count)

# exercise1 : با دو روش بالا تعداد اعداد فرد بین دو هزار تا پنجاه هزار را نمایش بده
# exercise 2: مجموع اعداد زوج بین دو هزار تا 3ه هزار را حساب نمایید
