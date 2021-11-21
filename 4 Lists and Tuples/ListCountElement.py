li = [1, 1, 1, 2, 3, 4, 1, 5, 4, 1]
count = 0
for i in li:
    if(i == 1):
        count = count + 1
    else:
        continue
print(count)
print(f"Or we can simply use li.count(1): ", li.count(1))