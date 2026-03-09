#!/usr/bin/python3
import sys
if __name__ == "__main__":

    count = len(sys.argv)
    sum = 0
    for i in range (1, count):
        sum = sum + int(sys.argv[i])
    print(sum)
