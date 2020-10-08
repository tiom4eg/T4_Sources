from random import choice
translate = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
data = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]


def start(n):
    if n > 16 or n < 4:
        return 0
    else:
        starter = data
        src = ""
        for i in range(n):
            elem = choice(starter)
            del starter[translate[elem]]
            src += elem
        return src


def result(numb: str, source):
    c, b = 0, 0
    for i in range(len(numb)):
        if numb[i] == source[i]:
            b += 1
        elif numb[i] in source:
            c += 1
    if b != len(source):
        return (c, b)
    else:
        return 0