#Program to check if the year is leap year or not
year = int(input("Enter a year here: "))

if (year % 400 == 0) and (year % 100 == 0):
    print("This is a Leap Year")
elif (year % 4 == 0) and (year % 100 != 0):
    print("This is a Leap Year")
else:
    print("This is not a Leap Year")