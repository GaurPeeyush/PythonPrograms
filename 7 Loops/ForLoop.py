li = ['banana', 'appple', 'mango', 'grapes']
for i in li:
    print(i)
print("\n")
#Range Function
for i in range (1, 8):
    print(i)
print("\n")
for i in range (1, 8, 2):
    print(i)
print("\n")
for i in range (10):
    print(i)
    if i == 5:
        break
print("\n")
print("Now this will print even integers by skipping odds")
for i in range (100):
    if i%2 != 0:
        continue
    print(i)
#using pass
if i>0:
    pass
