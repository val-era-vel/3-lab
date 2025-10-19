summa = 0
count = 0

while True:
    n = int(input())
    if n == 0:
        break
    summa += n
    count += 1

average = summa / count
print(average)



