def recursive(string, num):
    if num == 5:
        return
    print(string, num)
    recursive(string, num + 1)


recursive("Hello World", 0)