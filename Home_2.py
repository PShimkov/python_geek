#Задача 1
my_int = 5
my_float = 1.2
my_str = "String"
my_list = ['list', '2']
my_tuple = ('a', 'b2_3')
my_dict = {'city': 'Abakan', 'Republic': 'khakasia'}

full_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in enumerate(full_list, start=1):
    print(f'{i} is {type(i)}')
#Задача 2
my_list = list(input("Enter something: "))
if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = el
        i += 2
else:
    i = 0
    while i < len(my_list)- 1:
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = el
        i += 2
print(my_list)
#Задача 3
dict = {1: 'January Winter',
        2: 'February Winter',
        3: 'March Spring',
        4: 'April Spring',
        5: 'May Spring',
        6: 'June Summer',
        7: 'Jule Summer',
        8: 'August Summer',
        9: 'September Fall',
        10: 'October Fall',
        11: 'November Fall',
        12: 'December Winter'}
number_month = int(input(f'Enter number of month: '))
print(dict[number_month])

Li = [  '',
        'January Winter',
        'February Winter',
        'March Spring',
        'April Spring',
        'May Spring',
        'June Summer',
        'Jule Summer',
        'August Summer',
        'September Fall',
        'October Fall',
        'November Fall',
        'December Winter']
num_month = int(input(f'Enter number of month: '))
print(Li[num_month])
#Задача 4
my_str = input("Enter string: ")
a = my_str.split(' ')
for i, j in enumerate(a):
    if len(j) > 10:
        j = j[0:10]
    print(i, j)
#Задача 5
number_req = int(input("Enter number: "))
my_list = [7, 5, 3, 3, 2]
for index, number in enumerate(my_list):
    if number_req <= int(my_list[index]):
        continue
    my_list.insert(index, number_req)
    print(my_list)
    break
else:
    my_list.append(number_req)
    print(my_list)
#Задача 6
all_blanks = []
all_staff = {"Name item": "", "Price": "", "Number of staff": "", "Unit": ""}
all_analitic = {"Name item": [], "Price": [], "Number of staff": [], "Unit": []}
num = 0
while True:
    if input('For exit press Y, or press another buttom for continue: ').upper() == "Y":
        break
    num += 1
    for i in all_staff.keys():
        data = input('{}: '.format(i))
        all_staff[i] = int(data) if (i == "Price " or i == "Number of staff") else data
        all_analitic[i].append(all_staff[i])
        print('Some now: \n ')
    for key , value in all_analitic.items():#
        print(key, value)


