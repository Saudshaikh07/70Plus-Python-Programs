num = int(input("Enter a number here: "))
sum = 0

if num < 0:
    print("Enter a natural number!")
else:
    while num > 0:
        sum += num
        num -= 1
    print(sum)
