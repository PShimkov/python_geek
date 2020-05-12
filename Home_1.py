#Задача 1
a = str(input("Enter your number :"))
b = int(input("Enter your number :"))
print(a , b)

#Задача 2
time_in_sec = int(input("Enter your time in sec: "))
hours = time_in_sec // 3600
minutes = time_in_sec // 60 - (hours * 60)
sec = time_in_sec % 60
print(f"Now is {hours}:{minutes}:{sec} ")

#Задача 3
n = input("Enter your number :")
summ = int(n) + int(n+n) + int(n+n+n)
print(summ)

#Задача 4
number = input("Enter number: ")
x = 0
for i in number:
   while int(i) > x:
       x = int(i)
print(x)

#Задача 5
profit = float(input("Enter profit company :"))
lesion = float(input("Enter lesion company :"))
if profit>lesion:
   Revenue = profit - lesion
   Employees = int(input("Enternumber of employees: "))
   Revenue_Employees = Revenue/Employees
   print(f"Profit Employees : {Revenue_Employees}")
   print(f"Profit company : {Revenue}")
elif profit == lesion:
   print("Zero#")
else:
   Minus_Revenue = profit - lesion
   print(f"Lesion company : {Minus_Revenue}")

#Задача 6
a = float(input("Enter start: "))
b = float(input("Enter finish: "))
day = 1
if a > b:
    print(day)
while a < b:
    a = a + a/10
    day += 1
print(day)