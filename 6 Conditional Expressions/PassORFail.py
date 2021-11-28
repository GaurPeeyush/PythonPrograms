m1 = int(input("Enter the marks of 1st. subject\n"))
m2 = int(input("Enter the marks of 2nd. subject\n"))
m3 = int(input("Enter the marks of 3rd. subject\n"))
per = (m1 + m2 + m3)/3
if(per>33):
    if(m1>40 and m2>40 and m3>40):
        print("You're Pass")
        print(f"Your percentage is {per}%")
    else:
        print("You're Fail")
        print(f"Your percentage is {per}%")
else:
    print("You're Fail")