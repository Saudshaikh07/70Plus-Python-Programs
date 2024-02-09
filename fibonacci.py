a = 0
b = 1

numberRange = int(input("Enter the range for fibonacci series"))

if numberRange == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2, numberRange):
        c = a + b
        print(c)
        b = a
        a = c