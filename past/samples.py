# def calc_ave(name, scratch_score, app_inv_score, python_score):
#     average = (scratch_score + app_inv_score + python_score)/3
#     return f"{name}'s average is : {average}"

# name = input('enter your name: ')
# sc_score = float(input('enter scratch score: '))
# app_score = float(input('enter app inventor score: '))
# py_score = float(input('enter python score: '))


# result = calc_ave(name, sc_score, app_score, py_score)
# print(result)


# برنامه محاسبه هزینه بنزین تا مشهد
# ورودی : میزان مصرف خودرو
# خروجی برنامه : هزینه بنزین رفت و برگشت
# فاصله تهران تا مشهد 1000 کیلومتر
# بنرین تا 60 لیتر، لیتری 1500 و بیش از آن لیتری 3000 تومان محاسبه می شود.

# car_consumption = float(input("enter your car's gass consumptions: "))

# تابع اول برای محاسبه میران بنزین مصرف شده در مسافت مشخص


# def calc_consump(distance, car_consp):
#     litr = (distance * car_consp)/100
#     return litr

# محاسبه هزینه بنزین مصرفی در مسیر رفت و برگشت


# def calc_cost(litr):
#     if litr <= 60:
#         return litr * 1500
#     cost = (60 * 1500) + (litr - 60) * 3000
#     return cost


# litr = calc_consump(2000, car_consumption)
# cost = calc_cost(litr)
# print("your gass cost from tehran to mashhad is: ", cost)


# Exercise
# فرض کن مدرسه شما قرار است اردویی ببرد
# ورودی برنامه تعداد داوطلبان برای اردو می باشد
# خروجی برنامه هزینه اردو بازای هر برای نفر. یعنی هر نفر چقدر باید به مدرسه پول بدهد

# هزینه پذیرایی برای هر نفر 25 تومان
# هزینه ورودی برای هر نفر 20 تومان
# کرایه دربست برای هر دستگاه ون 200 تومان است
# هر ون 10 نفر ظرفیت دارد
# اگر یک ون پر نشود باز هم کرایه دربست باید پرداخت شود

# PAZIRAEE_COST = 25
# VOROUDI_COST = 20
# DARBAST = 200
# VAN_CAPACITY = 10


# def calc_van_number(student_count):
#     van_numbers = 0

#     van_numbers = student_count // VAN_CAPACITY
#     if student_count % VAN_CAPACITY != 0:
#         van_numbers += 1  # van_numbers = van_numbers + 1

#     return van_numbers


# def cost_per_student(van_num, st_count):
#     van_cost_per_student = van_num * DARBAST / st_count
#     return van_cost_per_student + PAZIRAEE_COST + VOROUDI_COST


# student_number = int(input("enter how many student's: "))
# van = calc_van_number(student_number)
# result = cost_per_student(van, student_number)
# print("trip cost per student is:", result)
