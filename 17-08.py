#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
"""
    1  2  3
    4  5  6
    7  8  9
    
    left_diar  = arr[0][0] + arr[1][1] + arr[2][2]
    right_diar = arr[0][2] + arr[1][1] + arr[2][0]
    
    1 2 3 4
    5 6 7 8
    3 4 5 6
    1 2 3 6
    
    left_diar  = arr[0][0] + arr[1][1] + arr[2][2] + arr[3][3]
    right_diar = arr[0][3] + arr[1][2] + arr[2][1] + arr[3][0]
    
"""


def diagonalDifference(arr):
    len_arr = len(arr)
    left_arr = []
    right_arr = []
    print("LENGTH ===> ", len_arr)
    for i in range(len_arr):
        for j in range(len_arr):
            # print(f"arr[{i}][{j}]  =====>", arr[i][j])
            if i == j:
                left_arr.append(arr[i][j])
                break

        right_arr.append(arr[i][len_arr - i - 1])

    # for k in range(len_arr):
    #     print(f"arr[{k}][{len_arr-k-1}] =====>", arr[k][len_arr-k-1])
    #     right_arr.append(arr[k][len_arr-k-1])

    print(f"Right Array =====> {right_arr} and sum is {sum(right_arr)}")
    print(f"Left Array =====> {left_arr} and sum is {sum(left_arr)}")

    return abs(sum(right_arr) - sum(left_arr))


if __name__ == '__main__':
    # arr = [[1,2,3], [4,5,6], [9,8,9]]
    arr = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 9, 8, 9], [9, 1, 2, 5]]

    result = diagonalDifference(arr)
    print(result)
