# 输入case数
rows = int(input())

for case in range(0, rows):
    try:
        num = int(input())
        if num == 1:
            print(2)
        else:
            a = 2
            b = 0
            for i in range(1, num):
                n2 = i * 2
                b = a + 2 * n2 + 1
                a = b
            print(b)
    except EOFError:
        break
