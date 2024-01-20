#Swaping the variables using temp method

firstVar = input("Enter the first variable here: ")
secondVar = input("Enter the second variable here: ")

print("The first variable before the swap is: ", firstVar)
print("The second variable before the swap is: ", secondVar)

temp = firstVar
firstVar = secondVar
secondVar = temp

print("The first variable after the swap is: ", firstVar)
print("The second variable after the swap is: ", secondVar)

#Swapping the variables using left, right method

newFirstVar = input("Enter a new first variable: ")
newSecondVar = input("Enter a new second variable: ")

print("The first variable before the swap is: ", newFirstVar)
print("The second variable before the swap is: ", newSecondVar)

newFirstVar, newSecondVar = newSecondVar, newFirstVar

print("The first variable after the swap is: ", newFirstVar)
print("The second variable after the swap is: ", newSecondVar)