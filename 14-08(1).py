#miniMaxSum HackerRank
def miniMaxSum(arr):
    l = sorted(arr)
    print(f"{sum(l[:4])} {sum(l[1:])}")


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9]
    miniMaxSum(arr=arr)
