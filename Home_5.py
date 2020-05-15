import json
#Задача 1
with open('test.txt', 'w') as f:
     while True:
         line = input('Write something: ')
         if line == '':
             break
         f.write(line + '\n')
#Задача 2
with open("test.txt", "r") as f:
        lines = f.readlines()
        print('bla:', len(lines))
        for num_line, line in enumerate(lines, start=1):
            print('{}  - {} '.format(num_line, len(line.split())))
#Задача 3
with open("test.txt", "r") as f:
    salaries = []
    lines = f.readlines()
    for line in lines:
        name, salary = line.split(' - ')#
        salaries.append(int(salary))
        if int(salary) < 20000:
            print(line, end='')
    print('True', sum(salaries) / len(salaries))

with open('eng.txt') as f:#
     lines = f.readlines()
#Задача 4
with open('rus.txt', 'w') as f:
     for line in lines:
         if '1' in line:
             line = line.replace('One', 'Один')
         elif '2' in line:
             line = line.replace('Two', 'Два°')
         elif '3' in line:
             line = line.replace('Three', 'трии')
         elif '4' in line:
             line = line.replace('Four', 'Четыре')
         f.write(line)
#Задача 5
with open("new_test.txt", "w") as f:
    list = input("enter numbers")
    f.write("Entered numbers" +list +'\n')
    list_2 = map(int, list.split())
    simm = sum(list_2)
    f.write('Sum numbers ' +str(simm))
    print("Summary entered numbers: ", simm)
print("End...")#
#Задача 6
my_dict = dict()
with open('new_test.txt') as f:
    lines = f.readlines()
    for line in lines:
        splitted_line = line.split()
        subject = splitted_line[0]
        sum_lessons = sum([int(x[:x.find('(#')]) for x in splitted_line[1:] if '(' in x])
        my_dict[subject] = sum_lessons
print(my_dict)
# Задача 7

frim_dic = []
average = []

with open("home_7.txt") as f:
    lines = f.readlines()
    for line in lines:
        name, form, reven, costs = line.split()
        profit = int(reven) - int(costs)
        frim_dic[name] = profit
        if profit > 0:
            average.append(profit)

average = sum(average) / len(average)
out_info = [frim_dic, {'average_profit': average}]

with open('7.json', 'w') as f_json:
    json.dump(out_info, f_json)

with open('7.json') as f_json:
    print(json.load(f_json))
