# class Person:

#     def __init__(self, name, salary):
#         #print("Konstructor works")
#         self.name = name
#         self.salary = salary

#     # def __del__(self):
#         #print("Destructor works")

#     def show_person(self):
#         print("Name: ", self.name)
#         print("Salary: ", self.salary)


# person1 = Person("Bill", 1100)

# person1.show_person()

# person2 = Person("Tom", 1350)
# person2.show_person()
# if person1.salary > person2.salary:
#     print(person1.name, " > ", person2.name)
# elif person1.salary < person2.salary:
#     print(person1.name, " < ", person2.name)
# else:
#     print(person1.name, " = ", person2.name)
import random
import requests
from lib.db import add_user, add_valyuts, vyvid_valut, dell_valut

URL = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"


def request(URL):
    responce = requests.get(URL)
    return responce.json()


cuurency = request(URL)


def zapov_valut(cuurency):
    for item in cuurency:
        ccy = str(item["ccy"])
        base_ccy = str(item["base_ccy"])
        buy = float(item["buy"])
        sale = float(item["sale"])
        add_valyuts(ccy, base_ccy, buy, sale)


class Person:
    def __init__(self, name, surname, age, card_number, pin, UA, USD, EUR, BTC):
        self.name = name
        self.surname = surname
        self.age = age
        self.card_number = card_number
        self.pin = pin
        self.UA = UA
        self.USD = USD
        self.EUR = EUR
        self.BTC = BTC

    def show_person(self):
        print("Name: ", self.name)
        print("Surname: ", self.surname)
        print("Age: ", self.age)
        print("Card number: ", self.card_number)
        print("PIN: ", self.pin)
        print("UA: ", self.UA)
        print("USD: ", self.USD)
        print("EUR: ", self.EUR)
        print("BTC: ", self.BTC)


def add_users():
    name = input("Enter NAME => ")
    surname = input("Enter Surname => ")
    age = int(input("Enter Age => "))
    UA = 0
    USD = 0
    EUR = 0
    BTC = 0
    card_number = random.randrange(100000000, 999999999)
    pin = random.randrange(1000, 9999)
    add_user(name, surname, age, card_number, pin, UA, USD, EUR, BTC)
    print(name, " ", surname, "\nYU Card number => ",
          card_number, "\nYU PIN => ", pin)


def menyu(cuurency):
    exit = True
    while exit:
        vyb = int(
            input("1.MY Menyu \t2. Kurs Valut\t3. NEV USER\t0. EXIT => "))
        # if vyb == 1:
        #     pin = int(input("Enter PIN => "))
        # eror = True
        # while eror:

        if vyb == 2:
            dell_valut()
            zapov_valut(cuurency)
            vyvid_valut()
        elif vyb == 3:
            add_users()
        elif vyb == 0:
            exit = False


menyu(cuurency)
