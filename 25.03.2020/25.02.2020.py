import random
import copy

# Оголосити list з 7 елементів типу int. Заповнити його випадковими значеннями в діапазоні [-12..+50] та вивести на екран.
# Підрахувати кількість відємних та додатніх елементів масиву.


# def zapov(a):
#     for i in range(0, 7):
#         a.append(random.randrange(-12, 50))
#     return a


# def vyvid(a):
#     for item in zsev:
#         print(item)


# def pidrah(a):
#     plys = 0
#     minus = 0
#     i = 0
#     for item in a:
#         if a[i] >= 0:
#             plys += 1
#         elif a[i] < 0:
#             minus += 1
#         i += 1
#     print("Plys => ", plys, "\nMinus => ", minus)


# zsev = []
# zapov(zsev)
# vyvid(zsev)
# pidrah(zsev)

# масив з 7 елементів типу int. Визначити суму парних елементів масиву
# def zapov(a):
#     for i in range(0, 7):
#         a.append(random.randrange(1, 50))
#     return a


# def parn(a):
#     parni = 0
#     kilk = 0
#     for item in a:
#         if item % 2 == 0:
#             parni += item
#             kilk += 1
#             print("Parni => ", item)
#     print("Kilkist parnyh => ", kilk)
#     print("Suma parnyh => ", parni)


# zsev = []
# zapov(zsev)
# parn(zsev)

# Дано масив А. Скопіювати елементи масиву А у масив В.
# def zapov(a):
#     for i in range(0, 7):
#         a.append(random.randrange(1, 20))
#     return a


# def vyvid(a, b):
#     print("==========1===========")
#     for item in a:
#         print(item)
#     print("==========2===========")
#     for item in b:
#         print(item)


# zsevcopy = []
# zsev = []
# zapov(zsev)
# vyvid(zsev, zsevcopy)
# print("/////////////DO//////////////")
# zsevcopy = copy.deepcopy(zsev)
# vyvid(zsev, zsevcopy)


# Дано одновимірний масив. Знайти найбільший та найменший елементи масиву та поміняти їх у масиві місцями.
def zapov(a):
    for i in range(0, 7):
        a.append(random.randrange(1, 20))
    return a


def vyvid(a):
    for item in a:
        print(item)


def min_max(a):
    i = 0
    mi = 0
    ma = 0
    mi_sym = 0
    ma_sym = 0
    for item in a:
        if item == min(a):
            mi = i-1
            mi_sym = item
            print("MIN = ", item)
        elif item == max(a):
            ma = i-1
            ma_sym = item
            print("MAX = ", item)
        i += 1
    a.insert(mi, ma_sym)
    a.insert(ma, mi_sym)
    return a


zsev = []
zapov(zsev)
vyvid(zsev)
min_max(zsev)
vyvid(zsev)
