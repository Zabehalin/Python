# 1 ++++++++++++++++++
# a = int(input("enter 1 symwol "))
# b = int(input("enter 2 symwol "))
# c = int(input("enter 3 symwol "))

# print ("a = ",a)
# print ("b = ",b)
# print ("c = ",c)

# print ("a+b+c = ",a + b + c)

# ==============  2 =================
# a = int(input("enter 1 symwol "))
# b = int(input("enter 2 symwol "))
# print ("ser aryf = ", (a+b)/2)

# =============== 3 ====================

# kil = int (input("Enter KM - "))
# print (kil ,"km = ",(kil * 1000),"metr")

# =============== 4 ====================

# print("    HI\nEnter VALUT")
# valut = input()
# print("Enter Obmin VALUT")
# valutObmin = input()
# print("Enter sum ", valut)
# val = float(input())
# if valut == "USD":
#     if valutObmin == "UA":
#         print(val, " ", valut, " = ", val*25.50, valutObmin)
#     elif valutObmin == "EUR":
#         print(val, " ", valut, " = ", val*0.93, valutObmin)

# elif valut == "EUR":
#     if valutObmin == "USD":
#         print(val, " ", valut, " = ", val*1.08, valutObmin)
#     elif valutObmin == "UA":
#         print(val, " ", valut, " = ", val*30, valutObmin)

# elif valut == "UA":
#     if valutObmin == "USD":
#         print(val, " ", valut, " = ", val*0.036, valutObmin)
#     elif valutObmin == "EUR":
#         print(val, " ", valut, " = ", val*0.033, valutObmin)


# ============================ 5 ===========================
# a = int(input("ENTER (A) "))
# b = int(input("ENTER (B) "))
# c = int(input("ENTER (C) "))
# if a > (0):
#     print("A ", a)
# if b > (0):
#     print("B ", b)
# if c > (0):
#     print("C ", c)
# ============================== 6 ===============================

a = int(input("ENTER (A) "))
b = int(input("ENTER (B) "))
c = int(input("ENTER (C) "))
if a == b:
    if a == c and a == b:
        print("A = B = C")
    elif a == b:
        print("A = B")
elif b == c:
    if b == c:
        print("B = C")
elif c == c:
    if b == c:
        print("B = C")
