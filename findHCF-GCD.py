# num1 = int(input("Enter the first number here: "))
#
# num2 = int(input("Enter the second number here:"))
#
# if num2>num1:
#     x = num1
#     y = num2
# else:
#     x = num2
#     y = num1
#
# for i in range(1, num1+1):
#     if (x % i == 0) and (y % i == 0):
#         hcf = i
#
# print(i)


def findHCF(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf


print("The HCF of given two numbers is : ", findHCF(12, 30))
