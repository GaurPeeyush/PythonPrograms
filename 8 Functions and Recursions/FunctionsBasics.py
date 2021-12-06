def percent(n, marks):
    sum = 0
    for i in range(n):
        sum = sum + marks[i]
    div = n*100
    p = sum*100/div
    return p

marks1 = [75, 98, 88, 78]
percentage = percent(4, marks1)
print(percentage)