''' Program to print the following pattern for n = 3 and continue accordingly
     ***
     **
     * '''
def pattern(n):
    for i in range(n):
        print("*" * (n-i))

n = int(input("Enter a number\n"))
pattern(n)