#Program to find the largest of three numbers:

firstNumber = float(input("Enter the first number here: "))
secondNumber = float(input("Enter the first number here: "))
thirdNumber = float(input("Enter the first number here: "))

if (firstNumber > secondNumber) and (firstNumber > thirdNumber):
    print("The largest of the three numbers is ", firstNumber)
elif (secondNumber > firstNumber) and (secondNumber > thirdNumber):
    print("The largest of the three numbers is ", secondNumber)
else:
    print("The largest of the three numbers is", thirdNumber)

