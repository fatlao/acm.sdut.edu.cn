# 输入case数
rows = int(input())

# 循环输入case

dict = {
    "A": "2", "B": "2", "C": "2",
    "D": "3", "E": "3", "F": "3",
    "G": "4", "H": "4", "I": "4",
    "J": "5", "K": "5", "L": "5",
    "M": "6", "N": "6", "O": "6",
    "P": "7", "R": "7", "S": "7",
    "T": "8", "U": "8", "V": "8",
    "W": "9", "X": "9", "Y": "9",
    "-": "", "Q": "", "Z": "",
    "0": "0", "1": "1", "2": "2",
    "3": "3", "4": "4", "5": "5",
    "6": "6", "7": "7", "8": "8",
    "9": "9"
}

# 统计map
sum = {}

for case in range(0, rows):
    # 输入case
    line = input()
    realnum = ""
    for c in line:
        realnum = realnum + dict[c]

    if realnum not in sum:
        sum[realnum] = 1
    else:
        sum[realnum] = sum[realnum] + 1

# 排序输出
tels = []
for k, v in sum.items():
    if v > 1:
        tels.append(k)

tels.sort()

if len(tels) > 0:
    for tel in tels:
        print(tel[0:3] + "-" + tel[3:] + " " + str(sum[tel]))
else:
    print("No duplicates.")
