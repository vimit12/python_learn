import re


# lonelyinteger HackerRank

def lonelyinteger(a):
    elements = dict()

    for i in a:
        if i in elements.keys():
            elements[i] = elements[i] + 1
        else:
            elements[i] = 1
    else:
        return list(filter((lambda x: x if elements[x] == 1 else 0), elements.keys()))[-1]


if __name__ == '__main__':
    a = [1, 2, 3, 4, 3, 2, 1]
    a = [34, 95, 34, 64, 45, 95, 16, 80, 80, 75, 3, 25, 75, 25, 31, 3, 64, 16, 31]
    result = lonelyinteger(a)
    print(result)
