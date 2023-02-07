#!/usr/bin/python3
for z in range(0, 10):
    for a in range(z + 1, 10):
        if z == 8 and a == 9:
            print("{}{}".format(z, a))
    break
        print("{}{}".format(z, a), end=", ")
