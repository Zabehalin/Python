# Написати функцію, яка порівнює два цілих числа і повертає результат порівняння в вигляді одного з знаків: <, > або =.


# def por(a, b):
#     if a > b:
#         result = " > "
#     elif b > a:
#         result = " < "
#     elif a == b:
#         result = " = "
#     return result


# a = int(input("Enter (A) = "))
# b = int(input("Enter (B) = "))

# res = por(a, b)
# print("(A)", res, "(B)")

# Написати функцію, яка отримує в якості параметрів два цілих числа і повертає суму чисел з діапазону між ними.
# def sum(a=0, b=0):
#     su = 0
#     i = a+1
#     while i < b:
#         print(i)
#         su += i
#         i += 1
#     return su


# a = int(input("Enter (A) = "))
# b = int(input("Enter (B) = "))
# res = sum(a, b)
# print("sum diapazon = ", res)

# 3. Написати функцію, яка обчислює вартість поїздки на автомобілі на дачу (туди і назад). Вхідними даними є: відстань до дачі (км);
#  кількість бензину, яку споживає автомобіль на 100 км пробігу; ціна одного літру бензину. Дані для розрахунків вводяться користувачем.
# def rozrahunok(kilom, benz, benzkm):
#     kilom * 2
#     benzkm / 100
#     benzkm * kilom
#     suma = benzkm * benz
#     return suma


# kilom = float(input("Enter KM = "))
# benz = float(input("Enter many Benz (1L) = "))
# benzkm = float(input("Benz 100 KM = "))
# suma = rozrahunok(kilom, benz, benzkm)
# print("Suma = ", suma)

# Написати калькулятор, робота якого буде основана на функціях.
# Введення цифр та вибір математичної операції виконати в діалоговому стилі
# (запитати у користувача, вивести меню). У програмі передбачити уникнення помилок
# (ділення на нуль і т.д.). Фантазія та «дизайн» меню – ціниться та вітається!!!
# Примітка! Кожна арифметична операція описується окремою функцією. Побудова самого меню також винесена в окрему функцію
def dodav(sym1, sym2):
    return sym1+sym2


def vidnim(sym1, sym2):
    return sym1-sym2


def mnoz(sym1, sym2):
    return sym1*sym2


def dilen(sym1, sym2):
    return sym1/sym2


exit = True
sym1 = float(input("sym = "))
while exit:
    vyb = int(input("1. (+)\t2. (-)\t3. (*)\t4. (/)\t0. (=)    "))
    if vyb == 0:
        print("SUM = ", sym1)
        exit = False

    sym2 = float(input("sym = "))
    if vyb == 3 and sym1 == 0 or vyb == 4 and sym1 == 0:
        print("EROR (*0)")
        exit = False
    elif vyb == 3 and sym2 == 0 or vyb == 4 and sym2 == 0:
        print("EROR (*0)")
        exit = False
    if vyb == 1:
        syma = dodav(sym1, sym2)
        sym1 = syma
    elif vyb == 2:
        syma = vidnim(sym1, sym2)
        sym1 = syma
    elif vyb == 3:
        syma = mnoz(sym1, sym2)
        sym1 = syma
    elif vyb == 4:
        syma = dilen(sym1, sym2)
        sym1 = syma
