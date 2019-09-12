# 输入case数
cardNumbers = int(input())
testcase = input()
cards = testcase.split(" ")

bucketAlice = {}
bucketBob = {}

alice = []
bob = []

if cardNumbers == 2:
    if cards[0] == cards[1]:
        print(1)
    else:
        print(0)
else:
    # 桶排序
    for i in range(0, len(cards)):
        n = int(cards[i])
        if i % 2 == 0:
            if n not in bucketAlice:
                bucketAlice[n] = 1
            else:
                bucketAlice[n] = bucketAlice[n] + 1
        else:
            if n not in bucketBob:
                bucketBob[n] = 1
            else:
                bucketBob[n] = bucketBob[n] + 1

    for k, v in bucketAlice.items():
        alice.append([k, v])

    for k, v in bucketBob.items():
        bob.append([k, v])


    def takeSecond(arr):
        return arr[0] * 100000 + arr[1]


    alice.sort(key=takeSecond, reverse=True)
    bob.sort(key=takeSecond, reverse=True)

    print(alice)
    print(bob)


    if alice[0][0] != bob[0][0]:
        # 第一多的数不相等
        print(cardNumbers - (alice[0][1] + bob[0][1]))
    else:
        # 第一多的数相等
        if alice[0][1] > bob[0][1]:
            # 第一多的次数不等
            print(cardNumbers - (alice[0][1] + bob[1][1]))
        elif alice[0][1] < bob[0][1]:
            # 第一多的次数不等
            print(cardNumbers - (bob[0][1] + alice[1][1]))
        else:
            # 第一多的次数相等,看第二多
            if len(alice) == 1 and len(bob) == 1:
                print(cardNumbers - alice[0][1])
            else :
                if alice[1][1] > bob[1][1]:
                    print(cardNumbers - (alice[1][1] + bob[0][1]))
                else:
                    print(cardNumbers - (bob[1][1] + alice[0][1]))
