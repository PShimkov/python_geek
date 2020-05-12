from functools import reduce
import sys
from itertools import count, cycle
from math import factorial
#Задача 1

houres, sallary, bonus = map(float, sys.argv[1:]) #map for taking all from parameters
print("Evry : {}".format(houres * sallary + bonus))

##Задача 2

my_list = [9, 7, 7, 75, 4, 546, 6]
new_list = [num for i, num in enumerate(my_list) if my_list[i] > my_list[i - 1] and i !=0]
print(new_list)

#Задача 3

new_gen = [x for x in range(24, 241) if x % 20 == 0 or x % 21 == 0]
print(new_gen)

#Задача 4

new_list = [1, 4,4, 6, 7, 1]
new_gen = [x for x in new_list if new_list.count(x) == 1]
print(new_gen)

#Задача 5

def red_fun(el_p, el):#
    return el_p* el

new_hen = [reduce(red_fun, [el for el in range(100, 1001) if el % 2 == 0])]
print(new_hen)

mi_list = [x for x in range(100, 1001) if x % 2 == 0]
reduce(red_fun, mi_list)
print(reduce(red_fun, mi_list))

##Задача

for i in count(int(input("enter ur number: "))):
    print(i)

my_list = [1, 2, 3, 4, 5, 6, 7]

for i in cycle(my_list):
   print(i)

#Задача 7

def fibo_gen():
    for el in count(1):
        yield factorial(el)

x = 0
for i in fibo_gen():
    print("Factorial {} - {}: ".format(x + 1, i))
    if x == 14:
        break
    x += 1
