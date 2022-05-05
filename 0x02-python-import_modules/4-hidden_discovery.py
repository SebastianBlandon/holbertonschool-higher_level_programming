#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    dir = dir(hidden_4)
    ex = "__"
    for i in range(1, len(dir)):
        if ex not in dir[i]:
            print(dir[i])
