# Using For Loop
number = int(input("Enter a number here: "))
factorial = 1

if number < 0:
    print("There is no factorials for negative numbers")
elif number == 0:
    print("The factorial of 0 is 1")
elif number > 0:
    for i in range(1, number + 1):
        factorial = factorial * i
    print("The factorial of the number is ", factorial)


# Finding the factorial using recursion

def fact(a):
    if a == 0:
        return 1
    else:
        return a * fact(a - 1)


number = int(input("Enter a number here: "))
result = fact(number)
print("The factorial of the number is: ", result)
