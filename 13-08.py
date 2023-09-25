#plusMinus Hacker Rank
import math
def plusMinus(arr):
    plus = 0
    minus = 0
    zero = 0
    len_arr = len(arr)
    for i in arr:
        if i < 0:
            minus += 1
        elif i > 0:
            plus += 1
        else:
            zero += 1
    else:
        print("{:.6f}".format(plus/len_arr))
        print("{:.6f}".format(minus/len_arr))
        print("{:.6f}".format(zero/len_arr))

plusMinus(arr=[-4, 3, -9, 0, 4, 1])
