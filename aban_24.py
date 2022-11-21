# numbers = [1, 2, 3, 4, 5]
# slice
# new_numbers = numbers[1:4]
# print(new_numbers)
# new_numbers = numbers[1:4:2]
# print(new_numbers)


# print even numbers in the list


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even_numbers = numbers[1::2]
# print("even numbers are: ", even_numbers)

#  to print odd numbers:

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even_numbers = numbers[0::2]
# print("odd numbers are: ", even_numbers)


# name = "soshian"
# print("first three characters are: ", name[:])
# print("first three characters are: ", name[0:3])
# print("first three characters are: ", name[:3])
# print("first three characters are: ", name[::2])
# print("first three characters are: ", name[::3])

# لیست ها می توانند اعضای متنفاوت داشته باشند یعنی اعضای لیست می توانند از جنس های مختلف باشند
# my_list = ['ali', 1, 'reza']

# لیست های تودرتو یعنی اعضای لیست می توانند خودشان هم یک لیست باشند
# numbers = [1, 2, 3, 4]
# strings = ['a', 'b', 'c']

# my_list = [numbers, strings]
# print(my_list)
# print(my_list[0])
# print(my_list[1])
# print(my_list[0][0])

#   چطور b را نمایش دهیم؟

# print(my_list[1][1])


# اضافه کردن به لیست

# numbers = [1, 2, 3, 4]
# numbers.append(5)
# numbers.append(6)
# numbers.append('a')
# numbers.append([0, -1, -2])
# print(numbers)

# تاپل

# numbers = (1, 2, 3, 4, 5)
# immutable
# numbers[0] = 10  # > error
# print(numbers[1:3])

# dictionary

students_favorites = {
    'javad': 'footbal',
    'ali': 'baseball',
    'nima': 'tennis'

}
print(type(students_favorites))
print('ali likes: ', students_favorites['ali'])
print('nima likes: ', students_favorites['nima'])
student = {
    'id': 1,
    'name': 'javad',
    'age': 15
}
print(student['name'], "is", student['age'], "years old")

# exercise: make three students as dictionary above, and then put them in to a list and print the list
students = []
student1 = {}
student2 = {}
student3 = {}
