#!/usr/bin/python3
import sys


def main():
    length = len(sys.argv)
    result = 0
    if length == 1:
        print("{}".format(result))
    elif length == 2:
        print("{}".format(result + sys.argv[1]))
    else:
        for i in range(1, length):
            result += int(sys.argv[i])
        print("{}".format(result))


if __name__ == "__main__":
    main()
