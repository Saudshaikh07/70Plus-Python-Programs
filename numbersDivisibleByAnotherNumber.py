#Solution 1:
num = int(input("Enter a number here: "))

for i in range(1,100):
    if i % num == 0:
        print(i)

#Solution 2

# l = [39,48,26,98,33,67,87]
#
# result = list(filter(lambda x : x % 13 == 0,l))
#
# print("The numbers divisible by 13 are: ", result)