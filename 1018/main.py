while True:
    try:
        num = int(input())
        if num == 1:
            print(1)
        elif num == 2:
            print(2)
        else:
            a = 1
            b = 2
            c = 0
            for i in range(2, num):
                c = a + b
                a = b
                b = c
            print(c)
    except EOFError:
        break
