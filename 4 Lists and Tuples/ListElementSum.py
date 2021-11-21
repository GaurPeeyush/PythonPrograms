li = []
n = int(input("Enter the number of elements in the list: \n"))
summ = 0 # don't use builtin names for your own variables! for ex: sum
for i in range (n):
    print("Enter the Element: ")
    li.append(int(input()))
    summ = summ + li[i]
print(f"List is: {li}")
print(f"The sum of elements is {summ}")
print("Or we can simply use sum(li): ", sum(li))