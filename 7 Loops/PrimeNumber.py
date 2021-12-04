n =  int(input("Enter the number\n"))
prime =  True
for i in range(2, n):
    if(n%i == 0):
        prime = False
        break
        
if (prime == True):
     print("Number is prime\n")
else:
    print("Number is not prime")
