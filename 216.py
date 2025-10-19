while True:
    n = int(input())
    for i in range(10, 100):
        if i % 10 == n and (i % 2 == 1 or n == 0):
            print(i, end=' ')
    print()

 