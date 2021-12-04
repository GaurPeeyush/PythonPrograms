'''print this pattern for n = 4 and accordingly
              *
             ***
            ***** 
           *******
'''
n = int(input("Enter a number\n"))
for i in range(n):
    print(" " *  (n-i-1), end ="")
    print("*" * (2*i+1), end ="")
    print(" " * (n-i-1))