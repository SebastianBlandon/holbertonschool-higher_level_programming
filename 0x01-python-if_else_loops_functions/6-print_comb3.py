#!/usr/bin/python3
for i in range(1, 89):
    if (i < 10):
        print("{0:0>2}".format(i), end=", ")
    elif ((i / 10) < i % 10):
        print("{}".format(i), end=", ")
i = i + 1
print(i)
