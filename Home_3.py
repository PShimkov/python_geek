#Задача 1
def my_func(x, y):
    try:
        x = int(x)
        y = int(y)
        result = x / y
    except ValueError:
        return "Value wrong"
    except ZeroDivisionError:
        return "Zero fall"
    return result

#Задача 2
def data_client(name, surname, year, city, email, phone_nymber):

    name = input(name)
    surname = input(surname)
    year = input(year)
    city = input(city)
    email = input(email)
    phone_nymber = input(phone_nymber)
    return ' '.join([name, surname, year, city, email, phone_nymber])

print(data_client('Name', 'Surname', "year", 'City', 'email', 'phone_nymber'))

def data_client2(**kwargs):
    return kwargs

print(data_client2( name = input("Enter name: "),
                    surname = input("Enter surname: "),
                    year = input("Enter year: "),
                    city = input("Enter city: "),
                    email = input("Enter email: "),
                    phone_nymber = input("Enter phone_nymber: ")))
#Задача 3
def summ(x, y, z):
    my_list = [x, y, z]
    my_list.pop(my_list.index(min(my_list)))
    return sum(my_list)

print(summ(7, 9, 10))

# Задача 4
def fun_pow(x, y):
    return x ** y

def fun_pow2(x, y):
    x, y = float(x), int(y)
    res = x
    for i in range(abs(y - 1)):
        res *= x
    return 1 / res

print(fun_pow2(5, 2))
#Задача 5
def my_sum ():
    ex = False
    result = 0
    while ex == False:
        numbers = input("Enter number or Q of exit: ").split()
        now_res = 0
        for num in numbers:
            if num == "q" or "Q" in num:
                ex = True
                break
            else:
                now_res += int(num)
        result += now_res
    print(result)

print(my_sum())
#Задача 6
def func_up():
    var = str(input("Enter string: ")).title()

    return var

print(func_up())