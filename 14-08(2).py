#timeConversion HackerRank
import re
def timeConversion(s):

    if re.findall(r"PM", s, re.IGNORECASE):
        time_arr = re.findall(r"(\d+):(\d+):(\d+)", s)[-1]
        if time_arr[0] == "12":
            return ":".join(time_arr)
        else:
            return str(int(time_arr[0])+12) + ":" + ":".join(time_arr[1:])
    else:
        time_arr = re.findall(r"(\d+):(\d+):(\d+)", s)[-1]
        if time_arr[0] == "12":
            return "00:" + ":".join(time_arr[1:])
        else:
            return ":".join(time_arr)


if __name__ == "__main__":
    s = "12:45:54PM"
    # s = "12:05:47AM"
    print(timeConversion(s=s))
