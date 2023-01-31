# about while loop

# for i in range(5):
#     print('ok')

# i = 0
# while i < 5:
#     print('ok')
#     i = i + 1  # i +=1


# numbers = [1, 2, 3]
# for n in numbers:
#     print('-')


# name = 'soshiyan'
# for i in range(len(name)):
#     print(name[i])


# infinite loop حلقه بی نهایت
# while True:
#     print('hi')


###################################################

'''
    *
   * *
  * * *
 * * * *
* * * * *
'''

# while

# i = 0
# while i < 5:
#     print(' '*(4-i) + ('* ')*(i+1))
#     i += 1
'''
*
* *
* * *
* * * *
* * *
* *
*
'''

i = 0

while i < 7:
    if i < 7/2:
        print('* ' * (i+1))
    else:
        print('* ' * (7-i))

    i += 1
'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *


'''