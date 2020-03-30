# Написати функцію, яка отримує дату (день, місяць) і виводить назву свята, що випадає на цей день
# (наприклад, 7.01 – Різдво, 9.05 – День Перемоги).
# Запрограмувати реакцію програми на 4 – 5 свят.


def data(a, b):
    if a == 1 and b == 1:
        print("New Year")
    elif a == 1 and b == 6:
        print("Christmas carol")
    elif a == 3 and b == 8:
        print("The eighth of March")
    elif a == 4 and b == 19:
        print("Easter")


exit = True
while exit:
    vyb = int(input("1. svato\t0. EXIT => "))
    if vyb == 0:
        exit = False
    elif vyb == 1:
        year = int(input("Enter YEAR => "))
        month = int(input("Enter MONTH => "))
        data(year, month)
