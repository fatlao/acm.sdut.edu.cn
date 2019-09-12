while True:
    try:
        line = input()
        args = line.split(" ")
        print(int(args[0]) + int(args[1]))
    except EOFError:
        break;

