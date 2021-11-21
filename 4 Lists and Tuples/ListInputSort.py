m = []
n = int(input("Enter the number of Students:\n"))
for i in range(n):
    print(f"Enter the marks of {i+1} student:")
    m.append(int(input()))
m.sort()
print(f"The sortred list of marks is {m}")