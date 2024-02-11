nterms = int(input("Enter the range of power here: "))

result = list(map(lambda x: 2 ** x, range(nterms+1)))

# print(result)

for i in range(nterms+1):
    print("2 to the power of ", i, "is", result[i])