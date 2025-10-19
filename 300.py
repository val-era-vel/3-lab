n = int(input())
bills = [64, 32, 16, 8, 4, 2, 1]
for bill in bills:
    count = n // bill
    if count > 0:
        n -= count * bill
        print(f"{count} ({bill})")




