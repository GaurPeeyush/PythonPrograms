n = int(input("Enter the number\n"))
mul = 1
if n < 0:
    print("Invalid")
else:
    for i in range(1, n+1):
        if n == 0:
            print("factorial = 1")
            break
        mul = mul * i
print(mul)
