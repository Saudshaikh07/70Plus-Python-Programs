lowerRange = int(input("Enter the lower range here: "))
upperRange = int(input("Enter the upper range here: "))

for num in range(lowerRange, upperRange+1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp = temp // 10
    if num == sum:
        print(num)