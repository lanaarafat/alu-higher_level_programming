#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = abs(number) % 10
if number < 0:
   num = -num
   print("Last digit of {} is {} and is ".format(number, num), end="")
if num > 5:
   print("Last digit of {} is {} and is greater than 5".format(number, num), end="")
elif num == 0:
   print("Last digit of {} is 0 and is 0".format(number, num), end="")
else:
   print("Last digit of {} is {} and is less than 6 and not 0")
