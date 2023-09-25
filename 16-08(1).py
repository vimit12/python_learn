import re
import math


# flippingBits HackerRank

def decimal_to_binary(n):
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n //= 2
    return binary


def flippingBits(n):
    result = decimal_to_binary(n)
    result = "0" * (32 - len(result)) + str(result) if len(result) < 32 else str(result)
    flip_list = ["1" if int(i) == 0 else "0" for i in result]
    return int("".join(flip_list), 2)


if __name__ == '__main__':
    n = 9
    print(flippingBits(n))
