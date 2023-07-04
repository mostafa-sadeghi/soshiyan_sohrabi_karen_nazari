x = [1, 2, 3, 4, 5, 9, 9, 9]

# print("first item:", x[0])
# print(f"first item: {x[0]}")

# print("last item:", x[-1])
# print("last item:", x[len(x)-1])
# print("last item:", x[5])
# print(f"last item: {x[-1]}")
# print(f"my slice: {x[:3]}")

# total = 0
# for number in x:
#     total += number

# print(f"total is : {total}")
# print(f"total is : {sum(x)}")
# print(f"x length is : {len(x)}")
# print(x)

# new_number = int(input("enter a number: "))
# x.append(new_number)
# print(x)

# new_number_to_delete = int(input("enter a number to delete: "))
# if new_number_to_delete in x:
#     x.remove(new_number_to_delete)

# for number in x:
#     if number == new_number_to_delete:
#         x.remove(number)

# x = list(set(x))
# my_list = []
# for number in x:
#     if number not in my_list:
#         my_list.append(number)
# x = my_list

# for number in x:
#     if number == new_number_to_delete:
#         x.remove(number)

# print(x)


# all_numbers = []
# total = 0
# for number in range(100,251):
#     if number % 3 == 0:
#         all_numbers.append(number)
#         if number % 2 == 1:
#             total += number

# print(f"total is: {total}")
# print(f"all numbers are: {all_numbers}")


# import turtle

# for i in range(3):
#     turtle.forward(100)
#     turtle.left(120)


# turtle.done()

person1 = {
    'name': "karen",
    'age': 14,
    'blood': 'B'
}

person2 = {
    'name': 'soshiyan',
    'age': 12,
    'blood': 'A'
}

persons = [person1, person2]

# print(persons[1]['age'])
# new_name = input("enter a name: ")
# new_age = int(input("enter age: "))
# new_blood = input("enter blood group: ")

# person3 = {
#     'name':new_name,
#     'age':new_age,
#     'blood':new_blood
# }
# persons.append(person3)
print(persons)
# del persons[0]
# del persons[0]
# persons.pop()
# persons.pop()
# print(persons)

new_name = input("enter the name: ")
for person in persons:
    if new_name == person['name']:
        print(f"{new_name} has {person['age']} years old")
