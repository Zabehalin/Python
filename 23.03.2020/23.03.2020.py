# Протягом тижня вимірювали температуру повітря. Знайти кількість днів, коли температура перевищувала 10o С.

# exit = True
# while exit:
#     for i in range(1, 8):
#         if i == 1:
#             Monday = int(input("Monday    ℃ = "))
#         elif i == 2:
#             Tuesday = int(input("Tuesday   ℃ = "))
#         elif i == 3:
#             Wednesday = int(input("Wednesday ℃ = "))
#         elif i == 4:
#             Thursday = int(input("Thursday  ℃ = "))
#         elif i == 5:
#             Friday = int(input("Friday    ℃ = "))
#         elif i == 6:
#             Saturday = int(input("Saturday  ℃ = "))
#         elif i == 7:
#             Sunday = int(input("Sunday    ℃ = "))
#     print("Dey > 10℃")
#     if Monday >= 10:
#         print("Monday    ℃ = ", Monday)
#     if Tuesday >= 10:
#         print("Tuesday   ℃ = ", Tuesday)
#     if Wednesday >= 10:
#         print("Wednesday ℃ = ", Wednesday)
#     if Thursday >= 10:
#         print("Thursday  ℃ = ", Thursday)
#     if Friday >= 10:
#         print("Friday    ℃ = ", Friday)
#     if Saturday >= 10:
#         print("Saturday  ℃ = ", Saturday)
#     if Sunday >= 10:
#         print("Sunday    ℃ = ", Sunday)
#     vybir = int(input("0. EXIT \n1. RESET  "))
#     if vybir == 0:
#         exit = False


# 2. Скласти програму ’Атракціони’. Програма запитує суму (грн.) у користувача.
#  Потім виводить на екран перелік доступних атракціонів.
#  Користувач обирає атракціон та ’оплачує’ його.
#  Вихід з програми при виборі пункту ’вихід’ або при недостатній сумі грошей.
# exit = True
# while exit:
#     erormany = True
#     while erormany:
#         many = int(input("Enter you many = "))
#         if many < 100:
#             print("EROR manuy min 100")
#         elif many >= 100:
#             erormany = False

#     print("Welcom to the \n    ATTRACTION")
#     exitt = True
#     while exitt:

#         vyb = int(input(
#             "1.Swing = 100 \n2.Trampoline = 150\n3.Dars = 180\n9.Reset games\n0.EXIT ATTRACTION\nENTER NEW GAMES"))
#         if vyb == 1:
#             print("Swing - 100")
#             many -= 100
#         elif vyb == 2:
#             print("Trampoline - 150")
#             many -= 150
#         elif vyb == 3:
#             print("Dars - 180")
#             many -= 180
#         elif vyb == 9:
#             exitt = False
#         elif vyb == 0:
#             exitt = False
#             exit = False
#         if many < 100:
#             print("EROR manuy min 100")
#             exitt = False


# Написати програму, яка виводит на екран 10 випадкових чисел у діапазоні від 0 до 17 і підраховує їх суму та добуток.
import random

# dobut = 1
# suma = 0
# for i in range(1, 11):
#     ra = random.randrange(1, 17)
#     print(ra)
#     suma += ra
#     dobut *= ra
# print("suma = ", suma, "\ndobutoc = ", dobut)

# Гра у кості. Гравці(комп’ютер і людина) кидають по 2 кубики. У кого сума на кубиках більша, той заробляє 1 бал.
# Якщо на кубиках дубль(подвоєння, тобто дві четвірки і т.і.), то гравець додатково заробляє 2 бали.
# Гра закінчується при наборі одним із гравцем N балів.

print("    Welcom")
exit = True
while exit:
    err = int(input("0. exit\n(ENTER) START"))
    if err == 0:
        exit = False
    erormany = True
    while erormany:
        many = int(input("Enter you many = "))
        if many < 100:
            print("EROR manuy min 100")
        elif many >= 100:
            erormany = False
    exitt = True
    while exitt:
        vybir = int(input("Enter stawka = "))
        manypc = 0
        manyuser = 0
        for i in range(1, 11):
            apc = random.randrange(1, 6)
            bpc = random.randrange(1, 6)
            print("PC = ", apc, "  ", bpc)
            if apc == bpc:
                manypc += (apc + bpc * 2)
            manypc += (apc + bpc)
            aaaa = input("Enter Peak")
            auser = random.randrange(1, 6)
            buser = random.randrange(1, 6)
            print("USER = ", auser, "  ", buser)
            if auser == buser:
                manyuser += (auser + buser * 2)
            manyuser += (auser + buser)
        if manypc > manyuser:
            print("    Won PC  ", manypc, " > ", manyuser)
            many -= vybir
            print("YOU MANY = ", many)
        elif manyuser > manypc:
            print("    Won USER  ", manyuser, " > ", manypc)
            many += vybir
            print("YOU MANY = ", many)
        elif manyuser == manypc:
            print("Someone's", manyuser, " = ", manypc)
        if many < 100:
            print("\nEROR manuy min 100")
            exitt = False
