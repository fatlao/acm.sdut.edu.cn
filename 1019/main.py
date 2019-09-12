while True:
    try:
        num = int(input())
        if num == 1:
            print(3)
        elif num == 2:
            print(8)
        else:
            a = 3
            b = 8
            c = 0
            for i in range(2, num):
                c = 2 * a + 2 * b
                a = b
                b = c
            print(c)
    except EOFError:
        break