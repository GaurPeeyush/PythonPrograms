a1 = int(input("Enter the first number:\n"))
a2 = int(input("Enter the second number:\n"))
a3 = int(input("Enter the third number:\n"))
a4 = int(input("Enter the fourth number:\n"))
if(a1>a2 and a1>a3 and a1>a4):
    print(a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print(a2)
elif(a3>a2 and a3>a1 and a3>a4):
    print(a3)
elif(a4>a2 and a4>a1 and a4>a3):
    print(a4)
else:
    print("NONE")