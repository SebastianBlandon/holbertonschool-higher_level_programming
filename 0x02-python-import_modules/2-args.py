#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if (len(sys.argv) <= 1):
        print("0 arguments.")
    else:
        if (len(sys.argv) == 2):
            print("1 argument:\n1:", sys.argv[1])
        elif (len(sys.argv) > 2):
            print(len(sys.argv) - 1, "arguments:")
        for i in range(1, len(sys.argv)):
            print(i, ":", sys.argv[i])
